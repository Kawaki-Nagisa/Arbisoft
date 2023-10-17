import React from "react";
import TicketCard from "./TicketCard";
import { updateTicketStage } from "./data";

export default function StageCard({ stageHeading, ticketCards, onDragEnd }) {
  return (
    <div className="bg-cyan-950/50 px-2 py-2 w-96 h-screen overflow-auto space-y-5">
      <h5 className="text-sm text-gray-500 font-medium text-gray-600">
        {stageHeading}
      </h5>
      <div className="space-y-5 flex flex-col justify-center items-center">
        {ticketCards.map((data, key) => (
          <TicketCard onClick={updateTicketStage} key={key} ticketData={data} />
        ))}
      </div>
    </div>
  );
}
