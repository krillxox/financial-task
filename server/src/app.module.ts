import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { AnalyzeModule } from './analyze/analyze.module';
import { ConfigModule } from '@nestjs/config';
import { DatabaseModule } from './config/database.config';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: `.env.${process.env.NODE_ENV || 'development'}`,
    }),
    DatabaseModule,
    AuthModule,
    AnalyzeModule
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
