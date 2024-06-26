// install (please try to align the version of installed @nivo packages)
// yarn add @nivo/line
import { ResponsiveLine } from "@nivo/line";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";
import { mockLineData as data } from "../data/mockData";
import { fetchAttackAction } from "../network/request";
import React, { useState, useEffect } from "react";

const LineChart = ({ isCustomLineColors = false, isDashboard = false }) => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	// Fetch the data using the external function
	const fetchData = async () => {
		try {
			const attackTypesData = await fetchAttackAction();
			setData(attackTypesData);
			setLoading(false);
		} catch (error) {
			console.error("Error fetching data", error);
			setError("Failed to fetch data from the API");
			setLoading(false);
		}
	};

	// Call the data-fetching function on component mount
	useEffect(() => {
		fetchData();
	}, []);

	// Return a loading message or error message if applicable
	if (loading) return <div>Loading...</div>;
	if (error) return <div>{error}</div>;

	return (
		<ResponsiveLine
			data={data}
			margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
			xScale={{ type: "point" }}
			yScale={{
				type: "linear",
				min: "auto",
				max: "auto",
				stacked: true,
				reverse: false,
			}}
			yFormat=" >-.2f"
			axisTop={null}
			axisRight={null}
			axisBottom={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "transportation",
				legendOffset: 36,
				legendPosition: "middle",
				truncateTickAt: 0,
			}}
			axisLeft={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "count",
				legendOffset: -40,
				legendPosition: "middle",
				truncateTickAt: 0,
			}}
			lineWidth={3}
			pointSize={10}
			pointColor={{ theme: "background" }}
			pointBorderWidth={2}
			pointBorderColor={{ from: "serieColor" }}
			pointLabelYOffset={-18}
			enableTouchCrosshair={true}
			useMesh={true}
			legends={[
				{
					anchor: "bottom-right",
					direction: "column",
					justify: false,
					translateX: 100,
					translateY: 0,
					itemsSpacing: 0,
					itemDirection: "left-to-right",
					itemWidth: 80,
					itemHeight: 20,
					itemOpacity: 0.75,
					symbolSize: 12,
					symbolShape: "circle",
					symbolBorderColor: "rgba(0, 0, 0, .5)",
					effects: [
						{
							on: "hover",
							style: {
								itemBackground: "rgba(0, 0, 0, .03)",
								itemOpacity: 1,
							},
						},
					],
				},
			]}
		/>
	);
};

export default LineChart;
