import { ResponsiveHeatMap } from "@nivo/heatmap";
import { useTheme } from "@mui/material";

import { tokens } from "../theme";

const data = [
	{
		id: "Japan",
		data: [
			{
				x: "Train",
				y: -98822,
			},
			{
				x: "Subway",
				y: 76562,
			},
			{
				x: "Bus",
				y: -14843,
			},
			{
				x: "Car",
				y: 97213,
			},
			{
				x: "Boat",
				y: 378,
			},
			{
				x: "Moto",
				y: 6395,
			},
			{
				x: "Moped",
				y: 13566,
			},
			{
				x: "Bicycle",
				y: -3355,
			},
			{
				x: "Others",
				y: -70882,
			},
		],
	},
	{
		id: "France",
		data: [
			{
				x: "Train",
				y: -27789,
			},
			{
				x: "Subway",
				y: -54879,
			},
			{
				x: "Bus",
				y: 19697,
			},
			{
				x: "Car",
				y: 65546,
			},
			{
				x: "Boat",
				y: -68034,
			},
			{
				x: "Moto",
				y: -23223,
			},
			{
				x: "Moped",
				y: 8493,
			},
			{
				x: "Bicycle",
				y: -28599,
			},
			{
				x: "Others",
				y: 81390,
			},
		],
	},
	{
		id: "US",
		data: [
			{
				x: "Train",
				y: 91756,
			},
			{
				x: "Subway",
				y: 5700,
			},
			{
				x: "Bus",
				y: -16095,
			},
			{
				x: "Car",
				y: -36670,
			},
			{
				x: "Boat",
				y: -39795,
			},
			{
				x: "Moto",
				y: -39299,
			},
			{
				x: "Moped",
				y: -96217,
			},
			{
				x: "Bicycle",
				y: -2649,
			},
			{
				x: "Others",
				y: 92525,
			},
		],
	},
	{
		id: "Germany",
		data: [
			{
				x: "Train",
				y: 65240,
			},
			{
				x: "Subway",
				y: -96972,
			},
			{
				x: "Bus",
				y: 70996,
			},
			{
				x: "Car",
				y: -4302,
			},
			{
				x: "Boat",
				y: 44704,
			},
			{
				x: "Moto",
				y: -46889,
			},
			{
				x: "Moped",
				y: -65119,
			},
			{
				x: "Bicycle",
				y: -58470,
			},
			{
				x: "Others",
				y: -27540,
			},
		],
	},
	{
		id: "Norway",
		data: [
			{
				x: "Train",
				y: 70910,
			},
			{
				x: "Subway",
				y: 47298,
			},
			{
				x: "Bus",
				y: -21826,
			},
			{
				x: "Car",
				y: -22806,
			},
			{
				x: "Boat",
				y: 40266,
			},
			{
				x: "Moto",
				y: -1442,
			},
			{
				x: "Moped",
				y: -62171,
			},
			{
				x: "Bicycle",
				y: -52277,
			},
			{
				x: "Others",
				y: 7703,
			},
		],
	},
	{
		id: "Iceland",
		data: [
			{
				x: "Train",
				y: 30587,
			},
			{
				x: "Subway",
				y: 98371,
			},
			{
				x: "Bus",
				y: 45348,
			},
			{
				x: "Car",
				y: -58217,
			},
			{
				x: "Boat",
				y: 14346,
			},
			{
				x: "Moto",
				y: -42530,
			},
			{
				x: "Moped",
				y: 49890,
			},
			{
				x: "Bicycle",
				y: 37399,
			},
			{
				x: "Others",
				y: 45172,
			},
		],
	},
	{
		id: "UK",
		data: [
			{
				x: "Train",
				y: -1235,
			},
			{
				x: "Subway",
				y: -33689,
			},
			{
				x: "Bus",
				y: -44987,
			},
			{
				x: "Car",
				y: 49703,
			},
			{
				x: "Boat",
				y: 78855,
			},
			{
				x: "Moto",
				y: -80168,
			},
			{
				x: "Moped",
				y: -28825,
			},
			{
				x: "Bicycle",
				y: 90958,
			},
			{
				x: "Others",
				y: -68660,
			},
		],
	},
	{
		id: "Vietnam",
		data: [
			{
				x: "Train",
				y: -45592,
			},
			{
				x: "Subway",
				y: -77523,
			},
			{
				x: "Bus",
				y: -44956,
			},
			{
				x: "Car",
				y: -97987,
			},
			{
				x: "Boat",
				y: 52723,
			},
			{
				x: "Moto",
				y: 86616,
			},
			{
				x: "Moped",
				y: -24404,
			},
			{
				x: "Bicycle",
				y: 8874,
			},
			{
				x: "Others",
				y: -62037,
			},
		],
	},
];

const HeatMap = () => {
	const colors = tokens();
	const theme = useTheme();

	return (
		<ResponsiveHeatMap
			data={data}
			margin={{ top: 60, right: 90, bottom: 60, left: 90 }}
			valueFormat=">-.2s"
			axisTop={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: -90,
				legend: "",
				legendOffset: 46,
				truncateTickAt: 0,
			}}
			axisRight={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "country",
				legendPosition: "middle",
				legendOffset: 70,
				truncateTickAt: 0,
			}}
			axisLeft={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "country",
				legendPosition: "middle",
				legendOffset: -72,
				truncateTickAt: 0,
			}}
			colors={{
				type: "diverging",
				scheme: "red_yellow_blue",
				divergeAt: 0.5,
				minValue: -100000,
				maxValue: 100000,
			}}
			emptyColor="#555555"
			legends={[
				{
					anchor: "bottom",
					translateX: 0,
					translateY: 30,
					length: 400,
					thickness: 8,
					direction: "row",
					tickPosition: "after",
					tickSize: 3,
					tickSpacing: 4,
					tickOverlap: false,
					tickFormat: ">-.2s",
					title: "Value →",
					titleAlign: "start",
					titleOffset: 4,
				},
			]}
		/>
	);
};

export default HeatMap;
