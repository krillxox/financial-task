import { MongooseModule } from '@nestjs/mongoose';
console.log(process.env.MONGO_URI);

export const DatabaseModule = MongooseModule.forRootAsync({
  useFactory: async () => ({
    uri: process.env.MONGO_URI || 'mongodb://localhost:27017/financial_ai', // change DB name as needed
    dbName: process.env.MONGO_DB_NAME || 'financial_ai',
  }),
});
