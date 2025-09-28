import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { AnalyzeModule } from './analyze/analyze.module';

@Module({
  imports: [AuthModule, AnalyzeModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
