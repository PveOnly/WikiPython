// database.js

const serverIP = '127.0.0.1:5000'; // Replace with your actual server IP

// Function to fetch data from the Flask API
export async function fetchData(url) {
	try {
		const response = await fetch(`http://${serverIP}${url}`);
		const data = await response.json();
		return data;
	} catch (error) {
		console.error('Error fetching data:', error);
		return null;
	}
}

// Function to fetch pandas data by table name and number of rows
export async function getPandasDataByRows(tableName, numRows) {
	const url = `/pandas/${tableName}/${numRows}`;
	const data = await fetchData(url);
	return data;
}

// Function to fetch all pandas data by table name
export async function getAllPandasData(tableName) {
	const url = `/pandas/${tableName}`;
	console.log(url);
	const data = await fetchData(url);
	console.log(data);
	return data;
}

// Function to fetch all pandas data by table name
export async function getAllCategories(tableName) {
	const url = `/test/${tableName}`;
	console.log(url);
	const data = await fetchData(url);
	console.log(data);
	return data;
}

// Function to fetch all pandas data by table name
export async function getAnyUrl(url) {
	const data = await fetchData(url);
	console.log(data);
	return data;
}

// Function to fetch a random url from python doc
export async function getRandomUrl() {
	const url = `/pandas/random`;
	const data = await fetchData(url);
	console.log(data);
	return data;
}
