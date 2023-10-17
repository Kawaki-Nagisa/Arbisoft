let ticketData = [
    {
        "TicketTitle": "Fix UI Bug",
        "ModuleTitle": "User Profile",
        "TicketID": "T12345",
        "StoryPoints": 5,
        "AssignedName": "John Doe",
        "Stage" : "DESIGN REVIEW"
    },
    {
        "TicketTitle": "Implement Feature X",
        "ModuleTitle": "Dashboard",
        "TicketID": "T12346",
        "StoryPoints": 8,
        "AssignedName": "Jane Smith",
        "Stage" : "ONGOING"
    },
    {
        "TicketTitle": "Update Database Schema",
        "ModuleTitle": "Database",
        "TicketID": "T12347",
        "StoryPoints": 3,
        "AssignedName": "Bob Johnson",
        "Stage" : "READY FOR DEV"
    },
    {
        "TicketTitle": "Optimize Code Performance",
        "ModuleTitle": "Backend",
        "TicketID": "T12348",
        "StoryPoints": 6,
        "AssignedName": "Alice Brown",
        "Stage" : "DEV IN PROGRESS"
    },
    {
        "TicketTitle": "Design Landing Page",
        "ModuleTitle": "UI/UX",
        "TicketID": "T12349",
        "StoryPoints": 4,
        "AssignedName": "Eva Wilson",
        "Stage" : "READY FOR QA"
    },
    {
        "TicketTitle": "Bug Testing",
        "ModuleTitle": "Quality Assurance",
        "TicketID": "T12350",
        "StoryPoints": 2,
        "AssignedName": "Chris Clark",
        "Stage" : "CODE REVIEW"
    },
    {
        "TicketTitle": "Feature Documentation",
        "ModuleTitle": "Documentation",
        "TicketID": "T12351",
        "StoryPoints": 1,
        "AssignedName": "David Lee",
        "Stage" : "DESIGN PREVIEW"
    },
    {
        "TicketTitle": "Security Audit",
        "ModuleTitle": "Security",
        "TicketID": "T12352",
        "StoryPoints": 7,
        "AssignedName": "Grace Taylor",
        "Stage" : "BACKLOG"
    },
    {
        "TicketTitle": "Integration Testing",
        "ModuleTitle": "Quality Assurance",
        "TicketID": "T12353",
        "StoryPoints": 2,
        "AssignedName": "Sophia Martin",
        "Stage" : "BACKLOG"
    },
    {
        "TicketTitle": "Add Payment Gateway",
        "ModuleTitle": "Payment Processing",
        "TicketID": "T12354",
        "StoryPoints": 9,
        "AssignedName": "Michael Wilson",
        "Stage" : "ONGOING"
    }
]

export function getTickets(){
    return ticketData
}

export function updateTicketStage(ticketID, newStage) {
    const ticketIndex = ticketData.findIndex((ticket) => ticket.TicketID === ticketID);
    
    if (ticketIndex !== -1) {
      ticketData[ticketIndex]["Stage"] = newStage;
      return true; // Ticket updated successfully
    }
    
    return false; // Ticket not found
  }
