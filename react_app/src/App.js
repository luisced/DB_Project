import React, { useState, useEffect, createContext } from "react";
import { ColorModeContext, useMode } from "./theme";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { Route, Routes } from "react-router-dom";
import axios from "axios";
import Topbar from "./views/global/Topbar";
import Dashboard from "./views/dashboard";
import CustomSidebar from "./views/global/Sidebar";
// import Bar from "./views/bar";
// import Form from "./views/Form";
// import Line from "./views/Line";
// import Pie from "./views/pie";
// import FAQ from "./views/faq";
// import Geography from "./views/geography";

function App() {
	const [theme, colorMode] = useMode();
	const [apiData, setApiData] = useState(null); // State to hold the fetched data

	useEffect(() => {
		// Function to fetch data
		const fetchData = async () => {
			try {
				const response = await axios.get("https://api.example.com/data");
				setApiData(response.data); // Set the fetched data into state
			} catch (error) {
				console.error("Error fetching API data: ", error);
			}
		};

		fetchData();
	}, []);

	return (
		<ColorModeContext.Provider value={colorMode}>
			<ThemeProvider theme={theme}>
				<CssBaseline />
				<div className="app">
					<CustomSidebar />
					<main className="content">
						<Topbar />
						<Routes>
							<Route path="/" element={<Dashboard />} />
							{/* <Route path="/team" element={<Team />} />
              <Route path="/contacts" element={<Contacts />} />
              <Route path="/invoices" element={<Invoices />} />
              <Route path="/form" element={<Form />} />
              <Route path="/bar" element={<Bar />} />
              <Route path="/pie" element={<Pie />} />
              <Route path="/line" element={<Line />} />
              <Route path="/faq" element={<FAQ />} />
              <Route path="/calendar" element={<Calendar />} />
              <Route path="/geography" element={<Geography />} /> */}
						</Routes>
					</main>
				</div>
			</ThemeProvider>
		</ColorModeContext.Provider>
	);
}

export default App;
