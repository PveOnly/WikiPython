<script>
	import { page, navigating, updated } from '$app/stores';
</script>

<nav>
	<a href="/" aria-current={$page.url.pathname === '/'}>home</a>
	<a href="/about">about</a>
	<a href="/test">test</a>
	<a href="/blog">blog</a>
	<a href="/todolist">todolist</a>
	<a href="/api">API</a>
	<a href="/post_todo">POST REQUEST TODO</a>
	<a href="/flask">FLASK</a>
	{#if $navigating}
		navigating to {$navigating.to.url.pathname}
	{/if}
</nav>

<slot />

{#if $updated}
	<p class="toast">
		A new version of the app is available

		<button on:click={() => location.reload()}> reload the page </button>
	</p>
{/if}
