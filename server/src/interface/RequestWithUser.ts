import type { Request } from 'express';

export interface RequestWithUser extends Request {
  user?: any; // or better: use a proper User type/interface
}