<script>
	/** @type {import('./$types').PageData} */
	export let data;
	/** @type {import('./$types').ActionData} */
	export let form;
	/** @type {Object} */
	let random_url;

	async function get_random_url() {
		const response = await fetch('/flask/random');
		random_url = await response.json();

	}
</script>

<form method="POST" action="?/login">
	<label>
		endpoint
		<input name="endpoint" type="endpoint" />
	</label>
</form>

<button on:click={get_random_url}>Get URL</button>

{#if random_url !== undefined}
	<p>You rolled a {random_url.random_url[1]}</p>
	<iframe title="TEST" src={random_url.random_url[1]} frameborder="0" scrolling="yes"></iframe>
{/if}

{#if form?.post}
	<!-- this message is ephemeral; it exists because the page was rendered in
           response to a form submission. it will vanish if the user reloads -->
	<p>DATA keys : {Object.keys(data)}</p>
	<p>DATA values user : {data.user}</p>
	<p>FORM post keys : {Object.keys(form.post)}</p>
	<p>FORM values post : {form.post}</p>

	<table>
		<thead>
			<tr>
				{#each form.post[0] as column}
					<th>{column}</th>
				{/each}
			</tr>
		</thead>
		<tbody>
			{#each form.post.slice(1) as row}
				<tr>
					{#each Object.values(row) as value}
						<td>{value}</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>
{/if}

<style scoped>
	th {
		text-align: left;
	}
	iframe {
		width: 100%;
		height: 100%;
		border: none; /* Removes the default border around the iframe */
		}
</style>