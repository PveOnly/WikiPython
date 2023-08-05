<script>
	/** @type {import('./$types').PageData} */
	export let data;
</script>

<!-- <h1>{data.post}</h1>
<div>{data.post[0]}</div>
<div>
	{#each Object.keys(data.post) as key}
		<p>{key}: {data.post[key]}</p>
	{/each}
</div> -->
{#if data?.post}
	<!-- this message is ephemeral; it exists because the page was rendered in
           response to a form submission. it will vanish if the user reloads -->
	<!-- <p>DATA keys : {Object.keys(data)}</p>
	<p>DATA values user : {data.user}</p>
	<p>FORM post keys : {Object.keys(data.post)}</p>
	<p>FORM values post : {data.post}</p> -->

	<table>
		<thead>
			<tr>
				{#each data.post[0] as column}
					<th>{column}</th>
				{/each}
			</tr>
		</thead>
		<tbody>
			{#each data.post.slice(1) as row}
				<tr>
					{#each Object.values(row) as value}
						<td>{value}</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>

	<style>
		th {
			text-align: left;
		}
	</style>
{/if}

<style>
	/* Reset some default styling */
	body,
	h1,
	h2,
	h3,
	p,
	table {
		margin: 0;
		padding: 0;
	}

	/* Add some spacing and a modern font */
	body {
		font-family: Arial, sans-serif;
		line-height: 1.6;
		background-color: #f4f4f4;
		padding: 20px;
	}

	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 20px;
	}

	/* Modern table styling */
	table {
		border-collapse: collapse;
		width: 100%;
		background-color: white;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}

	th,
	td {
		padding: 15px;
		text-align: left;
	}

	th {
		background-color: #f2f2f2;
		font-weight: 600;
	}

	tr:nth-child(even) {
		background-color: #f2f2f2;
	}

	/* Responsive styling */
	@media screen and (max-width: 600px) {
		table {
			border: 0;
		}

		table thead {
			display: none;
		}

		table tr {
			margin-bottom: 10px;
			display: block;
			border-bottom: 2px solid #ddd;
		}

		table td {
			display: block;
			text-align: right;
			padding: 10px;
		}

		table td::before {
			content: attr(data-label);
			float: left;
			font-weight: bold;
		}
	}
</style>
