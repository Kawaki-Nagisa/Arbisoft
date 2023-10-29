import React, { useEffect } from "react";
import DeviceThermostatIcon from "@mui/icons-material/DeviceThermostat";
import WaterDropIcon from "@mui/icons-material/WaterDrop";
import SpeedIcon from "@mui/icons-material/Speed";
import { connect } from "react-redux";

const WeatherGraph = ({ stateName, weatherData }) => {

  const defaultData = [
    {
      temperature: 291,
      pressure: 1013,
      humidity: 65,
    },
    {
      temperature: 293,
      pressure: 1015,
      humidity: 63,
    },
  ];

  if (!weatherData) {
    weatherData = defaultData;
  }
  if (!stateName) {
    stateName = "Default State";
  }

  return (
    <div className="bg-white h-fit w-fit p-10 rounded-lg shadow-lg space-y-20">
      <h1 className="text-3xl font-bold mb-4 text-center">{stateName}</h1>
      <div className="flex justify-between space-x-10">
        {weatherData.map((item, index) => (
          <div key={index} className="flex flex-col items-center">
            <div className="flex items-end justify-between w-32 h-40">
              <div
                className="w-8 bg-rose-600 items-center justify-center flex"
                style={{ height: item.temperature * 0.4 }}
              >
                <span className="text-rose-900 [writing-mode:vertical-rl]">
                  {item.temperature}
                </span>
              </div>
              <div
                className="w-8 bg-teal-600 items-center justify-center flex"
                style={{ height: item.pressure * 0.2 }}
              >
                <span className="text-teal-900 [writing-mode:vertical-rl]">
                  {item.pressure}
                </span>
              </div>
              <div
                className="w-8 bg-cyan-600 items-center justify-center flex"
                style={{ height: item.humidity * 2 }}
              >
                <span className="text-cyan-900 [writing-mode:vertical-rl]">
                  {item.humidity}
                </span>
              </div>
            </div>
            <div className="flex justify-center items-center space-x-6 mt-2">
              <div className="text-sm text-rose-800">
                <DeviceThermostatIcon />
              </div>
              <div className="text-sm text-teal-800">
                <SpeedIcon />
              </div>
              <div className="text-sm text-cyan-800">
                <WaterDropIcon />
              </div>
            </div>
            <div className="text-xl font-medium mb-2">Day - {index + 1}</div>
          </div>
        ))}
      </div>
    </div>
  );
};
const mapStateToProps = (state, ownProps) => {
  const index = ownProps.index;

  return {
    weatherData: state.weatherData[index],
    stateName: state.stateCoordinates[index]["State"],
  };
};
export default connect(mapStateToProps)(WeatherGraph);
