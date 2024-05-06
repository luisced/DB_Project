import { ResponsiveCalendar } from "@nivo/calendar";
import React, { useState, useEffect } from "react";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";
import { fetchAttackCalendar } from "../network/request"; // Adjust the path accordingly

const CalendarChart = () => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	const fetchData = async () => {
		try {
			const attackTypesData = await fetchAttackCalendar();
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
		<ResponsiveCalendar
			data={data}
			from="2020-03-01"
			to="2023-07-12"
			emptyColor="#eeeeee"
			colors={["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"]}
			margin={{ top: 40, right: 40, bottom: 40, left: 40 }}
			yearSpacing={20}
			monthBorderColor="#ffffff"
			dayBorderWidth={1}
			dayBorderColor="#ffffff"
			legends={[
				{
					anchor: "bottom-right",
					direction: "row",
					translateY: 36,
					itemCount: 4,
					itemWidth: 42,
					itemHeight: 36,
					itemsSpacing: 14,
					itemDirection: "right-to-left",
				},
			]}
		/>
	);
};

export default CalendarChart;
