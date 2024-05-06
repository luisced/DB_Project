import React, { useState, useEffect, createContext } from "react";
import axios from "axios";
import { ColorModeContext, useMode } from "./theme";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { Route, Routes } from "react-router-dom";
import Topbar from "./views/global/Topbar";
import Dashboard from "./views/dashboard";
import CustomSidebar from "./views/global/Sidebar";
import Bar from "./scenes/bar";
import Line from "./scenes/line";
import Pie from "./scenes/pie";
import Geography from "./scenes/geography";
import HeatMap from "./scenes/heatmap";
import { fetchAttackTypesByCountry } from "./network/request";

function App() {
	const [theme, colorMode] = useMode();
	const [apiData, setApiData] = useState(null); // Estado para almacenar los datos obtenidos de la API
	const url = "http://172.29.38.142:8000/cyber-attacks/"; // Asegúrate de que la URL es correcta y está completa

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await axios.get(url);
				const attackTypesData = await fetchAttackTypesByCountry();
				response.data.attackTypes = attackTypesData;
				setApiData(response.data);
				console.log("Data fetched", response.data);
				console.log("Attack types fetched", attackTypesData);
			} catch (error) {
				console.error("Error fetching data", error);
				// Manejo adicional de errores, como mostrar un mensaje en la interfaz de usuario
			}
		};

		fetchData();
	}, []); // Dependencias vacías para que se ejecute solo al montar el componente

	return (
		<ColorModeContext.Provider value={colorMode}>
			<ThemeProvider theme={theme}>
				<CssBaseline />
				<div className="app">
					<CustomSidebar />
					<main className="content">
						<Topbar />
						<Routes>
							<Route path="/" element={<Dashboard apiData={apiData} />} />
							<Route path="/bar" element={<Bar />} />
							<Route path="/line" element={<Line />} />
							<Route path="/geography" element={<Geography />} />
							<Route path="/heatmap" element={<HeatMap />} />
							<Route path="*" element={<Pie />} />
						</Routes>
					</main>
				</div>
			</ThemeProvider>
		</ColorModeContext.Provider>
	);
}

export default App;
