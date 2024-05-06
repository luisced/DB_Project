import { ResponsiveTreeMap } from "@nivo/treemap";

import { tokens } from "../theme";
import { useTheme } from "@mui/material";
import { mockPieData as data } from "../data/mockData";
import React, { useState, useEffect } from "react";
import { fetchAttackMostAttackedDevices } from "../network/request";

const TreeMapChart = () => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	const fetchData = async () => {
		try {
			const attackTypesData = await fetchAttackMostAttackedDevices();
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
	return (
		<ResponsiveTreeMap
			data={data}
			identity="name"
			value="loc"
			valueFormat=".02s"
			margin={{ top: 10, right: 10, bottom: 10, left: 10 }}
			labelSkipSize={12}
			labelTextColor={{
				from: "color",
				modifiers: [["darker", 1.2]],
			}}
			parentLabelPosition="left"
			parentLabelTextColor={{
				from: "color",
				modifiers: [["darker", 2]],
			}}
			borderColor={{
				from: "color",
				modifiers: [["darker", 0.1]],
			}}
		/>
	);
};

export default TreeMapChart;
