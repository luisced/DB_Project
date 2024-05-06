// BarChart.js

import React, { useState, useEffect } from "react";
import { ResponsiveBarCanvas } from "@nivo/bar";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";
import { fetchAttackTypesByCountry } from "../network/request"; // Adjust the path accordingly

const BarChart = () => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	// Fetch the data using the external function
	const fetchData = async () => {
		try {
			const attackTypesData = await fetchAttackTypesByCountry();
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
		<ResponsiveBarCanvas
			data={data}
			theme={{
				axis: {
					domain: {
						line: {
							stroke: colors.grey[100],
						},
					},
					legend: {
						text: {
							fill: colors.grey[100],
						},
					},
					ticks: {
						line: {
							stroke: colors.grey[100],
							strokeWidth: 1,
						},
						text: {
							fill: colors.grey[100],
						},
					},
				},
				legends: {
					text: {
						fill: colors.grey[100],
					},
				},
			}}
			// Adjust keys to match your data structure
			keys={["Intrusion", "Malware", "DDoS"]}
			indexBy="country"
			margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
			padding={0.3}
			valueScale={{ type: "linear" }}
			indexScale={{ type: "band", round: true }}
			colors={{ scheme: "nivo" }}
			borderColor={{
				from: "color",
				modifiers: [["darker", "1.6"]],
			}}
			axisTop={null}
			axisRight={null}
			axisBottom={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "Country",
				legendPosition: "middle",
				legendOffset: 32,
			}}
			axisLeft={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "Attack Type",
				legendPosition: "middle",
				legendOffset: -40,
			}}
			enableLabel={false}
			legends={[
				{
					dataFrom: "keys",
					anchor: "bottom-right",
					direction: "column",
					justify: false,
					translateX: 120,
					translateY: 0,
					itemsSpacing: 2,
					itemWidth: 100,
					itemHeight: 20,
					itemDirection: "left-to-right",
					itemOpacity: 0.85,
					symbolSize: 20,
					effects: [
						{
							on: "hover",
							style: {
								itemOpacity: 1,
							},
						},
					],
				},
			]}
			role="application"
			barAriaLabel={(e) =>
				`${e.id}: ${e.formattedValue} in country: ${e.indexValue}`
			}
		/>
	);
};

export default BarChart;
