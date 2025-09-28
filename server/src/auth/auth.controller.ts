import { Controller, Post, Body, Res, Req, UseGuards } from '@nestjs/common';
import { AuthService } from './auth.service';
import { Response, Request } from 'express';
import { JwtAuthGuard } from './jwt.strategy';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('signup')
  async signup(@Body() body: { email: string; password: string }) {
    return this.authService.signup(body);
  }

  @Post('login')
  async login(@Body() body: { email: string; password: string }, @Res({ passthrough: true }) res: Response) {
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
  @Post('check')
  checkAuth(@Req() req: Request) {
    return { authenticated: true, user: req.user };
  }
}
