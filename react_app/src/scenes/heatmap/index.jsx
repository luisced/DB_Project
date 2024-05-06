import { Box } from "@mui/material";
import Header from "../../components/Header";
import HeatMap from "../../components/HeatMap";

const Heat = () => {
	return (
		<Box m="20px">
			<Header title="Heat Map" subtitle="Simple Bar Chart" />
			<Box height="75vh">
				<BarChart />
			</Box>
		</Box>
	);
};

export default Heat;
