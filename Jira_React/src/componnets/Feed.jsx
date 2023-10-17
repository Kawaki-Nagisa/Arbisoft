import { Box, Stack, Typography } from "@mui/material";
import SideBar from "./SideBar";
import { StageCard } from ".";
import { stages } from "../utils/constants";
import { getTickets } from "./data.js";
import { useState } from "react";

const tickets = getTickets();
console.log(tickets)
const Feed = () => {
  const [selectedCategory,  setSelectedCategory] = useState("Board")


  return (
    <Stack sx={{ flexDirection: { sx: "column", md: "row" } }}>
      <Box
        sx={{
          height: { sx: "auto", md: "100vh" },
          borderRight: "1px solid #151515",
          px: { sx: 0, md: 2 },
        }}
      >
        <SideBar selectedCategory={selectedCategory} setSelectedCategory={setSelectedCategory}/>

        <Typography
          clanotssName="copyright"
          variant="body2"
          sx={{ mt: 1.5, color: "#fff" }}
        >
          Copyright © 2023 Kawaki X
        </Typography>
      </Box>

      <Box p={2} sx={{ overflowY: "auto", height: "90vh", flex: 2 }}>
        <Typography
          variant="h6"
          fontWeight="bold"
          mb={2}
          sx={{ color: "white" }}
        >
          <span style={{ color: "#FFF" }}>Jira Project Tickets</span>
        </Typography>

        <Box className="flex felx-row h-96 space-x-4 ">
          {stages.map((stage, key) => {
            const stageTickets = tickets.filter(
              (ticket) => ticket.Stage === stage.name
            );

            return (
              <StageCard
                key={key}
                stageHeading={stage.name}
                ticketCards={stageTickets}
              />
            );
          })}
        </Box>
      </Box>
    </Stack>
  );
};

export default Feed;
