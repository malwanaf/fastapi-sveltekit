<script lang="ts">
    import * as Card from "$lib/components/ui/card/index.js";
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input";
    import { Label } from "$lib/components/ui/label";
  
    let selectedFile: File | null = null;
    let imagePreviewUrl: string | null = null;
    let result: { filename: string; class: string; confidence: number } | null =
      null;
  
    function handleFileChange(e: Event) {
      const fileInput = e.target as HTMLInputElement;
      const file = fileInput.files?.[0];
      if (file) {
        selectedFile = file;
        imagePreviewUrl = URL.createObjectURL(file);
      }
    }
  
    async function handleUpload() {
      if (!selectedFile) return;
  
      const formData = new FormData();
      formData.append("image", selectedFile);
  
      const res = await fetch("http://localhost:8000/classify", {
        method: "POST",
        body: formData,
      });
  
      result = await res.json();
    }
  </script>
  
  <!-- Custom Dewe -->
  <Card.Root class="max-w-md mx-auto mt-10 shadow-lg mb-10">
    <Card.Content>
      <Label for="file">Select Image</Label>
      <Input
        id="file"
        type="file"
        accept="image/*"
        onchange={handleFileChange}
        class="mb-4 hover:bg-gray-100"
        placeholder="Select an image"
      />
      {#if imagePreviewUrl}
        <img
          src={imagePreviewUrl}
          alt="Preview"
          class="my-4 w-64 rounded shadow"
        />
      {/if}
  
      {#if result}
        <div class="my-6 p-4 border rounded shadow bg-gray-50">
          <p><strong>Filename:</strong> {result.filename}</p>
          <p><strong>Class:</strong> {result.class}</p>
          <p>
            <strong>Confidence:</strong>
            {(result.confidence * 100).toFixed(2)}%
          </p>
        </div>
      {/if}
    </Card.Content>
  
    <Card.Footer>
      <Button
        onclick={handleUpload}
        disabled={!selectedFile}
        class={!selectedFile ? " cursor-not-allowed" : ""}
      >
        Upload
      </Button>
    </Card.Footer>
  </Card.Root>
  