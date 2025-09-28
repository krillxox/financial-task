import { Controller, Post, Body, Res, Req, UseGuards, Get } from '@nestjs/common';
import { AuthService } from './auth.service';
import type { Response, Request } from 'express';
import { JwtAuthGuard } from './jwt.strategy';
import type { RequestWithUser } from 'src/interface/RequestWithUser';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('signup')
  async signup(@Body() body: { email: string; password: string }) {
    return this.authService.signup(body);
  }

  @Post('login')
  async login(
    @Body() body: { email: string; password: string },
    @Res({ passthrough: true }) res: Response,
  ) {
    const token = await this.authService.login(body);
    res.cookie('jwt', token, { httpOnly: true });
    return { message: 'Logged in' };
  }

  @Post('logout')
  async logout(@Res({ passthrough: true }) res: Response) {
    res.clearCookie('jwt');
    return { message: 'Logged out' };
  }

  @UseGuards(JwtAuthGuard)
  @Get('check')
  checkAuth(@Req() req: RequestWithUser) {
    return { authenticated: true, user: req.user };
  }
}
