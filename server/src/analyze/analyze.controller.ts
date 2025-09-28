import { Controller, Post, UploadedFile, UseInterceptors, UseGuards, Body } from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { AnalyzeService } from './analyze.service';
import { JwtAuthGuard } from '../auth/jwt.strategy';

@Controller('analyze')
export class AnalyzeController {
  constructor(private analyzeService: AnalyzeService) {}

  @UseGuards(JwtAuthGuard)
  @Post()
  @UseInterceptors(FileInterceptor('file'))
  async analyze(@UploadedFile() file: Express.Multer.File, @Body('query') query: string) {
    // Call your FastAPI endpoint here
    
    const result = await this.analyzeService.callFastAPI(file, query);

    return { result };
  }
}
