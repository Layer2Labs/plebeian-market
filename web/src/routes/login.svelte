<svelte:head>
    <title>Enter the Market</title>
</svelte:head>

<script>
    import { goto } from "$app/navigation";
    import Login from "../lib/components/Login.svelte";
</script>

<Login onLogin={() => goto("/auctions")} />
