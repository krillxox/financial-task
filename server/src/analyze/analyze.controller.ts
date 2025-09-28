import { Controller, Post, UploadedFile, UseInterceptors, UseGuards } from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { AnalyzeService } from './analyze.service';
import { JwtAuthGuard } from '../auth/jwt.strategy';

@Controller('analyze')
export class AnalyzeController {
  constructor(private analyzeService: AnalyzeService) {}

  @UseGuards(JwtAuthGuard)
  @Post()
  @UseInterceptors(FileInterceptor('file'))
  async analyze(@UploadedFile() file: Express.Multer.File) {
    // Call your FastAPI endpoint here
    const result = await this.analyzeService.callFastAPI(file);
    return { result };
  }
}
