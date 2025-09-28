import {
  Injectable,
  CanActivate,
  ExecutionContext,
  UnauthorizedException,
} from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { RequestWithUser } from 'src/interface/RequestWithUser';

@Injectable()
export class JwtAuthGuard implements CanActivate {
  constructor(private jwtService: JwtService) {}

  canActivate(context: ExecutionContext): boolean {
    const request: RequestWithUser = context.switchToHttp().getRequest();
    console.log(request.cookies);

    const token = request.cookies?.jwt; // read JWT from cookie

    if (!token) {
      throw new UnauthorizedException('No JWT token found');
    }

    try {
      const payload = this.jwtService.verify(token, {
        secret: process.env.JWT_SECRET || 'secretKey', // set your JWT secret in env
      });
      request.user = payload; // attach payload to request
      return true;
    } catch (err) {
      throw new UnauthorizedException('Invalid JWT token');
    }
  }
}
