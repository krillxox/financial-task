import { Injectable } from '@nestjs/common';
import axios from 'axios';
import FormData from 'form-data';

@Injectable()
export class AnalyzeService {
  async callFastAPI(file: Express.Multer.File) {
    const formData = new FormData();
    formData.append('file', file.buffer, file.originalname);

    const response = await axios.post('http://localhost:8000/analyze', formData, {
      headers: formData.getHeaders(),
    });

    return response.data;
  }
}
