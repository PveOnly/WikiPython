import { json } from '@sveltejs/kit';
import * as db from '$lib/server/flask_database.js';

export async function GET() {
	// TODO register the user
	console.log('ASS RANDOM');
	return json({
		random_url: await db.getRandomUrl()
	});
}
