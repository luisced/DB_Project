import { useState } from "react";
import { Sidebar, Menu, MenuItem } from "react-pro-sidebar";
// import "react-pro-sidebar/dist/css/styles.css";
import { Box, IconButton, Typography, useTheme } from "@mui/material";
import { Link } from "react-router-dom";
import { tokens } from "../../theme";
import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
import PeopleOutlinedIcon from "@mui/icons-material/PeopleOutlined";
import ContactsOutlinedIcon from "@mui/icons-material/ContactsOutlined";
import ReceiptOutlinedIcon from "@mui/icons-material/ReceiptOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import CalendarTodayOutlinedIcon from "@mui/icons-material/CalendarTodayOutlined";
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
import BarChartOutlinedIcon from "@mui/icons-material/BarChartOutlined";
import PieChartOutlineOutlinedIcon from "@mui/icons-material/PieChartOutlineOutlined";
import TimelineOutlinedIcon from "@mui/icons-material/TimelineOutlined";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import MapOutlinedIcon from "@mui/icons-material/MapOutlined";
import SolarPowerIcon from "@mui/icons-material/SolarPower";
const Item = ({ title, to, icon, selected, setSelected }) => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	return (
		<MenuItem
			active={selected === title}
			style={{
				color: selected === title ? "#6870fa" : colors.grey[200],
				backgroundColor:
					selected === title ? colors.primary[900] : "transparent",
				borderRadius: "10px",
			}}
			onClick={() => setSelected(title)}
			icon={icon}
		>
			<Link
				to={to}
				style={{
					textDecoration: "none",
					color: "inherit",
					display: "flex",
					alignItems: "center",
				}}
			>
				<Typography>{title}</Typography>
			</Link>
		</MenuItem>
	);
};

const CustomSidebar = () => {
	const theme = useTheme();
	const colors = tokens(theme.palette.mode);
	const [isCollapsed, setIsCollapsed] = useState(false);
	const [selected, setSelected] = useState("Dashboard");

	return (
		<Sidebar
			collapsed={isCollapsed}
			backgroundColor={colors.primary[400] + " !important"}
			rtl={false}
			style={{
				"& .pro-icon-wrapper": {
					backgroundColor: "transparent !important",
				},
			}}
		>
			<Menu
				iconShape="square"
				menuItemStyles={{
					button: ({ level, active, disabled }) => {
						if (level === 0) {
							return {
								color: disabled ? "#eee" : "#455A64",
								"&:hover": {
									backgroundColor: "#868dfb !important",
									color: "white !important",
									borderRadius: "8px !important",
									fontWeight: "bold !important",
								},
							};
						}
					},
				}}
			>
				{/* LOGO AND MENU ICON */}
				<MenuItem
					onClick={() => setIsCollapsed(!isCollapsed)}
					icon={isCollapsed ? <MenuOutlinedIcon /> : undefined}
					style={{
						margin: "10px 0 20px 0",
						color: colors.grey[100],
					}}
				>
					{!isCollapsed && (
						<Box
							display="flex"
							justifyContent="space-between"
							alignItems="center"
							ml="15px"
						>
							<Typography variant="h3" color={colors.grey[100]}>
								ADMIN
							</Typography>
							<IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
								<MenuOutlinedIcon />
							</IconButton>
						</Box>
					)}
				</MenuItem>

				{!isCollapsed && (
					<Box mb="25px">
						<Box display="flex" justifyContent="center" alignItems="center">
							<img
								alt="profile-user"
								width="100px"
								height="100px"
								src="https://avatars.githubusercontent.com/u/63626850?s=400&u=fa33bb8f5585086580fbafb58c60cb1e407aa7d2&v=4"
								style={{ cursor: "pointer", borderRadius: "50%" }}
							/>
						</Box>
						<Box textAlign="center">
							<Typography
								variant="h2"
								color={colors.grey[100]}
								fontWeight="bold"
								sx={{ m: "10px 0 0 0" }}
							>
								Luis Cedillo
							</Typography>
							<Typography variant="h5" color={colors.greenAccent[500]}>
								VP Fancy Admin
							</Typography>
						</Box>
					</Box>
				)}

				<Box paddingLeft={isCollapsed ? undefined : "10%"}>
					<Item
						title="Dashboard"
						to="/"
						icon={<HomeOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>

					<Typography
						variant="h6"
						color={colors.grey[300]}
						sx={{ m: "15px 0 5px 20px" }}
					>
						Data
					</Typography>
					<Item
						title="Heat Map"
						to="/heatmap"
						icon={<PeopleOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="Contacts Information"
						to="/contacts"
						icon={<ContactsOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="Invoices Balances"
						to="/invoices"
						icon={<ReceiptOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>

					<Typography
						variant="h6"
						color={colors.grey[300]}
						sx={{ m: "15px 0 5px 20px" }}
					>
						Pages
					</Typography>
					<Item
						title="Profile Form"
						to="/form"
						icon={<PersonOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="Calendar"
						to="/calendar"
						icon={<CalendarTodayOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="FAQ Page"
						to="/faq"
						icon={<HelpOutlineOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>

					<Typography
						variant="h6"
						color={colors.grey[300]}
						sx={{ m: "15px 0 5px 20px" }}
					>
						Charts
					</Typography>
					<Item
						title="Bar Chart"
						to="/bar"
						icon={<BarChartOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="Pie Chart"
						to="/pie"
						icon={<PieChartOutlineOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="Line Chart"
						to="/line"
						icon={<TimelineOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
					<Item
						title="Geography Chart"
						to="/geography"
						icon={<MapOutlinedIcon />}
						selected={selected}
						setSelected={setSelected}
					/>
				</Box>
			</Menu>
		</Sidebar>
	);
};

export default CustomSidebar;
