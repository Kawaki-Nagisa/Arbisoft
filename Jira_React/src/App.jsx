import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Box } from "@mui/material";

import { Feed } from "./componnets";

const App = () => (
  <BrowserRouter>
    <Box sx={{ backgroundColor: "#181b21" }}>
      <Routes>
        <Route path="/" exact element={<Feed />} />
      </Routes>
    </Box>
  </BrowserRouter>
);

export default App;
