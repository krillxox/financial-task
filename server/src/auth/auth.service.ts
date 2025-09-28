import { Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { User } from '../schema/user.schema'; // Mongoose schema
import * as bcrypt from 'bcrypt';
import { Model } from 'mongoose';
import { InjectModel } from '@nestjs/mongoose';

@Injectable()
export class AuthService {
  constructor(
    @InjectModel(User.name) private userModel: Model<User>,
    private jwtService: JwtService
  ) {}

  async signup({ email, password }) {
    const hash = await bcrypt.hash(password, 10);
    const user = new this.userModel({ email, password: hash });
    await user.save();
    return { message: 'User created' };
  }

  async login({ email, password }) {
    const user = await this.userModel.findOne({ email });
    if (!user || !(await bcrypt.compare(password, user.password))) {
      throw new Error('Invalid credentials');
    }
    return this.jwtService.sign({ sub: user._id });
  }
}
