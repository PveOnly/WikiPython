<script>
	// /** @type {number} */
	let number;

	async function roll() {
		const response = await fetch('/api/roll');
		number = await response.json();
	}
</script>

<button on:click={roll}>Roll the dice</button>

{#if number !== undefined}
	<p>You rolled a {number.random_url}</p>
{/if}
