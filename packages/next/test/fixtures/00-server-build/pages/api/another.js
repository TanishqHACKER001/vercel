export default (req, res) => {
  res.json({
    query: req.query,
    page: 'api/another.js',
    random: Math.random() + Date.now(),
    memory: process.env.AWS_LAMBDA_FUNCTION_MEMORY_SIZE,
  });
};
