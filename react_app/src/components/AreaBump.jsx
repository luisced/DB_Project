import { ResponsiveAreaBump } from "@nivo/bump";

import React, { useState, useEffect } from "react";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";
import { fetchAttackTypesOverTime } from "../network/request"; // Adjust the path accordingly

const AreBumpChart = () => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	const fetchData = async () => {
		try {
			const attackTypesData = await fetchAttackTypesOverTime();
			setData(attackTypesData);
			setLoading(false);
		} catch (error) {
			console.error("Error fetching data", error);
			setError("Failed to fetch data from the API");
			setLoading(false);
		}
	};

	useEffect(() => {
		fetchData();
	}, []);

	// Return a loading message or error message if applicable
	if (loading) return <div>Loading...</div>;
	if (error) return <div>{error}</div>;

	return (
		<ResponsiveAreaBump
			data={data}
			margin={{ top: 40, right: 100, bottom: 40, left: 100 }}
			spacing={8}
			colors={{ scheme: "nivo" }}
			blendMode="multiply"
			defs={[
				{
					id: "dots",
					type: "patternDots",
					background: "inherit",
					color: "#38bcb2",
					size: 4,
					padding: 1,
					stagger: true,
				},
				{
					id: "lines",
					type: "patternLines",
					background: "inherit",
					color: "#eed312",
					rotation: -45,
					lineWidth: 6,
					spacing: 10,
				},
			]}
			fill={[
				{
					match: {
						id: "CoffeeScript",
					},
					id: "dots",
				},
				{
					match: {
						id: "TypeScript",
					},
					id: "lines",
				},
			]}
			startLabel="id"
			endLabel="id"
			axisTop={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "",
				legendPosition: "middle",
				legendOffset: -36,
				truncateTickAt: 0,
			}}
			axisBottom={{
				tickSize: 5,
				tickPadding: 5,
				tickRotation: 0,
				legend: "",
				legendPosition: "middle",
				legendOffset: 32,
				truncateTickAt: 0,
			}}
		/>
	);
};

export default AreBumpChart;
