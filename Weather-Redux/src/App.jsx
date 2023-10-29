import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Box } from "@mui/material";
import { fetchCoordinates, fetchWeatherData } from "./actions";
import { Feed, SearchBar } from "./componnets";
import usaStates from "./utils/constants";

const App = () => {
  const dispatch = useDispatch();
  const coordinates = useSelector((state) => state.stateCoordinates);

  const handleSearch = async (state) => {
    try {
      if (usaStates.includes(state)) {
        await dispatch(fetchCoordinates(state));
      } else {
        window.alert("Invalid state entered. Please enter a valid US state.");
      }
    } catch (error) {
      window.alert("Error fetching coordinates.");
    }
  };

  useEffect(() => {
    if (coordinates && coordinates.length > 0) {
      const lastCoordinates = coordinates[coordinates.length - 1];
      dispatch(
        fetchWeatherData(lastCoordinates["Lat"], lastCoordinates["Lon"])
      );
    }
  }, [coordinates]);

  return (
    <BrowserRouter>
      <div className="bg-gray-200 text-center font-bold text-4xl">
        Weather - Redux
      </div>
      <SearchBar onSearch={handleSearch} />
      <Box className="bg-gray-400">
        <Routes>
          <Route path="/" element={<Feed />} />
        </Routes>
      </Box>
    </BrowserRouter>
  );
};

export default App;
