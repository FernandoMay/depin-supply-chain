import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Backend TypeScript is running!');
});

app.post('/item/register', (req, res) => {
  const { id, location, timestamp, status } = req.body;
  console.log(`Registering item: ${id}, ${location}, ${timestamp}, ${status}`);
  // Here you would interact with Starknet contracts or a database
  res.status(200).json({ id, location, timestamp, status });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
