import * as db from '$lib/server/flask_database.js';

/** @type {import('./$types').PageServerLoad} */
export async function load({ cookies }) {
	const user = cookies.get('sessionid');
	return { user };
}

/** @type {import('./$types').Actions} */
export const actions = {
	login: async ({ cookies, request }) => {
		const data = await request.formData();
		const url = data.get('endpoint');
		console.log(url);
		return {
			post: await db.fetchData(url)
		};
	},
	random: async (event) => {
		// TODO register the user
		console.log('ASS RANDOM');
		return {
			random_url: await db.getRandomUrl()
		};
	}
};
