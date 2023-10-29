import { Box, Stack } from "@mui/material";
import WeatherGraph from "./WeatherGraph";
import { useSelector } from "react-redux";
import { useEffect, useState } from "react";

const Feed = () => {
  const { weatherData, stName } = useSelector((state) => ({
    weatherData: state.weatherData,
    stName: state.stateCoordinates,
  }));
  const [renderWeatherGraphs, setRenderWeatherGraphs] = useState(false);

  useEffect(() => {
    if (
      weatherData.length !== 0 &&
      stName.length !== 0 &&
      weatherData.length === stName.length
    ) {
      setRenderWeatherGraphs(true);
    } else {
      setRenderWeatherGraphs(false);
    }
  }, [weatherData, stName]);

  return (
    <Stack>
      <Box className="flex flex-col space-y-10 justify-center items-center py-24">
        {renderWeatherGraphs &&
          stName.map((data, index) => (
            <WeatherGraph key={index} index={index} />
          ))}
      </Box>
    </Stack>
  );
};

export default Feed;
