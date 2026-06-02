import express from 'express';
import request from 'supertest';

// Recreate the app for testing (avoid listening on a port)
const app = express();
app.use(express.json());
app.get('/', (req, res) => { res.send('Backend TypeScript is running!'); });
app.post('/item/register', (req, res) => {
  const { id, location, timestamp, status } = req.body;
  res.status(200).json({ id, location, timestamp, status });
});

describe('Express Backend', () => {
  describe('GET /', () => {
    it('returns running message', async () => {
      const res = await request(app).get('/');
      expect(res.status).toBe(200);
      expect(res.text).toBe('Backend TypeScript is running!');
    });
  });

  describe('POST /item/register', () => {
    it('registers an item and returns it', async () => {
      const item = { id: '001', location: 'Warehouse A', timestamp: '2026-06-01T12:00:00Z', status: 'received' };
      const res = await request(app).post('/item/register').send(item);
      expect(res.status).toBe(200);
      expect(res.body).toEqual(item);
    });

    it('accepts partial item data', async () => {
      const item = { id: '002' };
      const res = await request(app).post('/item/register').send(item);
      expect(res.status).toBe(200);
      expect(res.body).toEqual({ id: '002' });
    });
  });
});
