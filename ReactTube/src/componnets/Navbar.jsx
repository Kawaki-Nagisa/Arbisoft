import { Stack, Typography } from "@mui/material";
import { Link } from "react-router-dom";

import { logo } from "../utils/constants";
import { SearchBar } from "./";

const Navbar = () => (
  <Stack
    direction="row"
    alignItems="center"
    p={2}
    sx={{
      position: "sticky",
      background: "#151515",
      top: 0,
      gap: "20%",
    }}
  >
    <Stack direction="row" alignItems="center" p={2}>
      <Link to="/" style={{ display: "flex", alignItems: "center" }}>
        <img src={logo} alt="logo" height={45} />
      </Link>
      <Typography variant="h3" fontWeight="bold" sx={{ color: "white" }}>
        React Tube
      </Typography>
    </Stack>
    <SearchBar />
  </Stack>
);

export default Navbar;
