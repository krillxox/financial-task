import { Injectable } from '@nestjs/common';
import { fetch, FormData } from 'undici';
// import FormData from 'form-data';

@Injectable()
export class AnalyzeService {
  async callFastAPI(file: Express.Multer.File, query: string) {
    const formData = new FormData();
    console.log(file);
    const uint8Array = new Uint8Array(file.buffer);
    formData.set('file', new File([uint8Array], file.originalname));
    formData.set('query', query);

    const response = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      return data;
    }
  }
}
