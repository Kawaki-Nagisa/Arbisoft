import React from "react";
import { useState } from "react";

const classMapping = [
  {
    bg: "bg-orange-950",
    tx: "text-orange-300",
  },
  {
    bg: "bg-sky-950",
    tx: "text-sky-300",
  },
  {
    bg: "bg-teal-300",
    tx: "text-teal-950",
  },
  {
    bg: "bg-violet-950",
    tx: "text-violet-300",
  },
];

export default function TicketCard({ ticketData }) {
  const [isPopupOpen, setPopupOpen] = useState(false);

  const firstChar = ticketData.ModuleTitle.charAt(0).toUpperCase();
  const index = firstChar.charCodeAt(0) % classMapping.length;
  const classes = classMapping[index];

  const openPopup = () => {
    setPopupOpen(true);
  };

  const closePopup = () => {
    setPopupOpen(false);
  };

  return (
    <div>
      <div
        onClick={openPopup}
        className="bg-neutral-700 text-xs w-52 px-2 py-3 space-y-2 rounded overflow-hidden shadow-lg text-left"
      >
        <div className="text-cyan-700">
          <h3 className="font-bold mb-2">{ticketData.TicketTitle}</h3>
        </div>
        <div
          className={`text-sm ${classes.bg} w-fit rounded px-1 ${classes.tx} font-bold`}
        >
          <p className="">{ticketData.ModuleTitle}</p>
        </div>
        <div className="flex flex-row justify-between items-center">
          <h4 className="text-slate-200">{ticketData.TicketID}</h4>
          <div className="text-white flex flex-row space-x-2">
            <p className=" rounded-full bg-neutral-600 px-1 flex items-center justify-center">
              {ticketData.StoryPoints}
            </p>
            <span className="h-7 w-7 bg-fuchsia-900 text-white flex items-center justify-center rounded-full">
              {ticketData.AssignedName[0]}
            </span>
          </div>
        </div>
      </div>

      {isPopupOpen && (
        <div className="fixed top-0 left-0 w-screen h-screen bg-gray-800 bg-opacity-50 flex justify-center items-center">
          <div className="bg-neutral-700 p-4 rounded-lg shadow-lg space-y-5 flex flex-col justify-center items-center">
            <h3 className="text-cyan-700 font-bold mb-2">
              {ticketData.TicketTitle}
            </h3>
            <p
              className={`text-sm ${classes.bg} w-fit rounded px-1 ${classes.tx} font-bold`}
            >
              {ticketData.ModuleTitle}
            </p>
            <h4 className="text-slate-200">Ticket ID: {ticketData.TicketID}</h4>
            <p className="text-white">Story Points: {ticketData.StoryPoints}</p>
            <p className="text-white font-bold">
              Assigned Name: {ticketData.AssignedName}
            </p>
            <p
              className={`text-sm ${classes.bg} w-fit rounded px-1 ${classes.tx} font-bold`}
            >
              Current Stage: {ticketData.Stage}
            </p>

            <button
              className="mt-4 bg-fuchsia-900 text-white px-4 py-2"
              onClick={closePopup}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
