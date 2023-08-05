import * as db from '$lib/server/flask_database.js';
/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	console.log('PASS');
	return {
		post: await db.getAllPandasData(params.category)
	};
}
