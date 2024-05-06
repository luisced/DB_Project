// network/request.js

import axios from "axios";

const API_URL = "http://172.29.38.142:8000/cyber-attacks/";

// Function to fetch attack types by country
export const fetchAttackTypesByCountry = async () => {
	const url = API_URL + "attack-types/"; // Adjust to your endpoint
	try {
		const response = await axios.get(url);
		return response.data; // Assuming data is returned as JSON
	} catch (error) {
		console.error("Error fetching attack types", error);
		throw error;
	}
};

export const fetchAttackTypesOverTime = async () => {
	const url = API_URL + "severity-over-time/";
	try {
		const response = await axios.get(url);
		return response.data; // Assuming data is returned as JSON
	} catch (error) {
		console.error("Error fetching attack types", error);
		throw error;
	}
};

export const fetchAttackCalendar = async () => {
	const url = API_URL + "calendar-heatmap/";
	try {
		const response = await axios.get(url);
		return response.data; // Assuming data is returned as JSON
	} catch (error) {
		console.error("Error fetching attack types", error);
		throw error;
	}
};

export const fetchAttackProtocolFrecuency = async () => {
	const url = API_URL + "protocol-frequency/";
	try {
		const response = await axios.get(url);
		return response.data; // Assuming data is returned as JSON
	} catch (error) {
		console.error("Error fetching attack types", error);
		throw error;
	}
};

export const fetchAttackMostAttackedDevices = async () => {
	const url = API_URL + "most-attacked-devices/";
	try {
		const response = await axios.get(url);
		return response.data; // Assuming data is returned as JSON
	} catch (error) {
		console.error("Error fetching attack types", error);
		throw error;
	}
};

export const fetchAttack = async () => {
	const url = API_URL + "most-attacked-devices/";
	try {
		const response = await axios.get(url);
		return response.data; // Assuming data is returned as JSON
	} catch (error) {
		console.error("Error fetching attack types", error);
		throw error;
	}
};
