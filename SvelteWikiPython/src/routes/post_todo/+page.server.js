import * as database from '$lib/server/database_v2.js';

export function load({ cookies }) {
	let userid = cookies.get('userid');

	if (!userid) {
		userid = crypto.randomUUID();
		cookies.set('userid', userid, { path: '/post_todo/' });
	}

	return {
		todos: database.getTodos(userid)
	};
}
