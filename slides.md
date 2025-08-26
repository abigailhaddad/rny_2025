---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Processing Document Collections with LLMs
  A practical workflow for handling large-scale document processing
drawings:
  persist: false
transition: slide-left
title: Processing Document Collections with LLMs
mdc: true
download: true
exportFilename: document-processing-llms
export:
  format: pdf
  timeout: 30000
  withClicks: false
  dark: true
---

# Processing Document Collections with LLMs
## A Practical Workflow

**Abigail Haddad**

---
layout: default
---

# Every Organization Has Documents
## (and the same questions about all of them)

<div class="grid grid-cols-3 gap-8 mt-12">
  <div class="text-center p-6">
    <div class="text-7xl mb-4">🏥</div>
    <p class="text-2xl font-semibold">Medical Records</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">👤</div>
    <p class="text-2xl font-semibold">Resumes</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">💬</div>
    <p class="text-2xl font-semibold">Customer Complaints</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">⚠️</div>
    <p class="text-2xl font-semibold">Error Logs</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">📄</div>
    <p class="text-2xl font-semibold">Contracts</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">📊</div>
    <p class="text-2xl font-semibold">Reports</p>
  </div>
</div>

---
layout: default
---

# Agenda

<div class="text-3xl space-y-6 mt-12">
  <p>📌 The Project</p>
  <p>📌 The Larger Problem</p>
  <p>📌 Applying This Pattern</p>
  <p>📌 What I Learned</p>
  <p>📌 Evaluation</p>
  <p>📌 Building A Couple More Blocks</p>
</div>

---
layout: section
---

# Part 1: The Project


---
layout: default
---

# Regulations.gov Comments

<div class="flex flex-col items-center justify-center">
  <img src="/images/regulations.jpg" style="width: 90%; height: auto;" />
</div>

---
layout: default
---

# What Did the Comments Say?

<div class="grid grid-cols-2 gap-12 mt-16">
  <div class="bg-green-100 border-4 border-green-500 rounded-lg p-12 text-center">
    <div class="text-6xl font-bold text-green-700">AGREE</div>
    <div class="text-8xl mt-4 text-green-700">✓</div>
  </div>
  
  <div class="bg-red-100 border-4 border-red-500 rounded-lg p-12 text-center">
    <div class="text-6xl font-bold text-red-700">DISAGREE</div>
    <div class="text-8xl mt-4 text-red-700">✗</div>
  </div>
</div>

---
layout: default
---

# My Deadline

<div class="flex flex-col items-center justify-center">
  <img src="/images/hourglass.png" class="w-95 h-95" />
</div>

---
layout: default
---

# My Usual Blocks

<div class="flex flex-col items-center justify-center">
<img src="/images/my usual blocks.png" class="w-90 h-90" />

</div>

---
layout: two-cols
---

# The Weird Stuff

📄 Dark scanned PDFs

🎭 Random meme attachments  

📸 Blurry photos of handwritten notes

::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/meme.webp" class="max-w-sm" />
</div>

---
layout: center
---

# I Added a New Block


<div class="flex flex-col items-center justify-center">
<img src="/images/ocr.png" class="w-90 h-90" />
</div>

---
layout: center
---

# I Occasionally Got Gibberish

<div class="flex flex-col items-center justify-center">
<img src="/images/is this text.png" class="w-90 h-90" />
</div>

---
layout: center
---

# So I Built a Gibberish Detector

<div class="flex flex-col items-center justify-center">
<img src="/images/gibberish detector blocks.png" class="w-90 h-90" />
</div>

---
layout: center
---

# Now I'm Debugging My Gibberish Detector

<div class="flex flex-col items-center justify-center">
<img src="/images/debugging.png" class="w-90 h-90" />
</div>

---
layout: center
---

# Finally, I Try Gemini To Extract Text...

```python
if extraction_fails(doc):
    result = gemini.process(doc)
```

---
layout: center
class: text-center
---

# It Works!! 🎉🎊🥳

---
layout: center
---

# Gemini Initially Cost Me Seven Cents

<div class="flex flex-col items-center justify-center">
<img src="/images/seven cents.png" class="w-90 h-90" />
</div>

---
layout: default
---

# The Results

<div class="grid grid-cols-3 gap-8 mt-12 text-center">
  <div class="border-2 rounded-lg p-6">
    <div class="text-6xl font-bold">33,647</div>
    <div class="text-2xl">Against</div>
    <div class="text-gray-500">(94%)</div>
  </div>
  
  <div class="border-2 rounded-lg p-6">
    <div class="text-6xl font-bold">1,596</div>
    <div class="text-2xl">Support</div>
    <div class="text-gray-500">(4.5%)</div>
  </div>
  
  <div class="border-2 rounded-lg p-6">
    <div class="text-6xl font-bold">306</div>
    <div class="text-2xl">Neutral</div>
    <div class="text-gray-500">(0.9%)</div>
  </div>
</div>

<div class="mt-8 text-center text-xl">
  Many "support" comments were duplicates/campaigns
</div>

---
layout: center
---

# Here It Is
  

<div class="flex flex-col items-center justify-center">
  <img src="/images/comment_site.jpg" style="width: 70%; height: auto;" />
</div>

---
layout: section
---

# Part 2: The Larger Problem

---
layout: default
---

# Every Organization Has Documents

<div class="grid grid-cols-3 gap-8 mt-12">
  <div class="text-center p-6">
    <div class="text-7xl mb-4">🏥</div>
    <p class="text-2xl font-semibold">Medical Records</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">👤</div>
    <p class="text-2xl font-semibold">Resumes</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">💬</div>
    <p class="text-2xl font-semibold">Customer Complaints</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">⚠️</div>
    <p class="text-2xl font-semibold">Error Logs</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">📄</div>
    <p class="text-2xl font-semibold">Contracts</p>
  </div>
  
  <div class="text-center p-6">
    <div class="text-7xl mb-4">📊</div>
    <p class="text-2xl font-semibold">Reports</p>
  </div>
</div>

---
layout: default
---

# Same Question Every Time

- Is this fraudulent? → **yes/no**
- What's the complaint about? → **category**
- Does this candidate qualify? → **yes/no + reason**
- What's the root cause? → **specific issue**

---
layout: center
---

# The Answer? Document Processing Pipeline

<div class="flex flex-col items-center justify-center">
<img src="/images/pipeline.png" class="w-100 h-100" />
</div>

---
layout: two-cols
---

# The Three Steps

### GET
Pull text from PDFs, Word docs, APIs, or user input

### PROCESS
Use LLMs, regex, BERT, or other tools to extract meaning

### DO
Create visualizations, populate templates, or trigger actions

::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/get process do blocks.png" />
</div>

---
layout: default
---

# Getting Back ONLY "Agree" or "Disagree"

<div class="flex flex-col items-center justify-center">
  <img src="/images/enumblock.png" style="width: 30%; height: auto;" />
</div>

**Enums → Structured output → Wrangleable results**

---
layout: default
---

# LiteLLM Structured Output + Pydantic

<div class="flex flex-col items-center justify-center">
  <img src="/images/structured output.jpg" style="width: 60%; height: auto;" />
</div>

---
layout: default
---

# Put Anything You Want in The Prompt

<div class="flex flex-col items-center justify-center">
  <img src="/images/longprompt.jpg" style="width: 80%; height: auto;" />
</div>

---
layout: default
---

# What I Actually Extracted

- **Stance**: agree / disagree / neutral-other
- **Themes**: multi-class classification
- **Summary**: unstructured text
- **Representative quote**: actual text
- **Reasoning**: why this classification

---
layout: section
---

# Part 3: Applying This Pattern

---
layout: default
---

# 📄 Your Documents

<div class="space-y-6 mt-12 text-2xl">
  <p>✓ Clean PDFs?</p>
  <p>✓ Scanned images?</p>
  <p>✓ Mixed formats?</p>
  <p>✓ Handwritten?</p>
</div>

---
layout: default
---

# 🎯 Your Goals

<div class="space-y-6 mt-12 text-2xl">
  <p>→ Extract fields?</p>
  <p>→ Classify docs?</p>
  <p>→ Summarize?</p>
  <p>→ Find patterns?</p>
</div>

---
layout: default
---

# Your Constraints

<div class="grid grid-cols-2 gap-4 mt-10">
  <div class="text-center p-8">
    <div class="text-6xl mb-4">🔒</div>
    <h3 class="text-3xl font-bold">Privacy</h3>
    <p class="text-2xl mt-2">Can data leave?</p>
  </div>
  
  <div class="text-center p-8">
    <div class="text-6xl mb-4">💰</div>
    <h3 class="text-3xl font-bold">Budget</h3>
    <p class="text-2xl mt-2">API costs OK?</p>
  </div>
  
  <div class="text-center p-8">
    <div class="text-6xl mb-4">⏰</div>
    <h3 class="text-3xl font-bold">Time</h3>
    <p class="text-2xl mt-2">One-off or ongoing?</p>
  </div>
  
  <div class="text-center p-8">
    <div class="text-6xl mb-4">📊</div>
    <h3 class="text-3xl font-bold">Explain</h3>
    <p class="text-2xl mt-2">Show your work?</p>
  </div>
</div>

---
layout: center
---

# Should I Throw It Into an LLM?

---
layout: center
---

<div class="text-6xl font-bold text-center">
  🤔 MAYBE!!! 🎲
</div>

---
layout: default
---

# Remember My Seven Cents?

**Gemini only worked because:**

<div class="space-y-4 mt-8">
  <p class="text-2xl">✓ Data could leave my environment</p>
  <p class="text-2xl">✓ 35,000 documents, most with no attachments = small enough for the budget</p>
</div>

<div class="mt-12 text-center">
  <p class="text-3xl font-bold border-2 p-6 rounded-lg inline-block">
    Different constraints = Different solution
  </p>
</div>

---
layout: default
---

# Your Toolkit

<div class="grid grid-cols-3 gap-6 mt-8">
  <div class="border rounded p-4">
    <h3 class="font-bold text-xl mb-3">GET</h3>
    <ul class="text-sm space-y-1">
      <li>PyPDF2, pdfplumber</li>
      <li>Tesseract OCR</li>
      <li>BeautifulSoup</li>
      <li>APIs</li>
    </ul>
  </div>
  
  <div class="border rounded p-4">
    <h3 class="font-bold text-xl mb-3">PROCESS</h3>
    <ul class="text-sm space-y-1">
      <li>OpenAI, Claude, Gemini</li>
      <li>BERT</li>
      <li>Regex</li>
    </ul>
  </div>
  
  <div class="border rounded p-4">
    <h3 class="font-bold text-xl mb-3">DO</h3>
    <ul class="text-sm space-y-1">
      <li>Quarto</li>
      <li>Email/Slack alerts</li>
      <li>API endpoints</li>
    </ul>
  </div>
</div>

---
layout: section
---

# Part 4: What I Learned

---
layout: center
---

# Start Simple

<div class="flex flex-col items-center justify-center">
<img src="/images/get process do blocks.png" class="w-80 h-80" />
</div>
  Build only the blocks you need

---
layout: default
---

# You Can't Build All The Blocks


<div class="flex flex-col items-center justify-center">
<img src="/images/too many blocks.png" class="w-70 h-70" />
</div>

---
layout: default
---

# Scaling Up

<div class="grid grid-cols-2 gap-12 mt-16">
  <div class="text-center">
    <div class="text-8xl mb-6">🛡️</div>
    <h3 class="text-3xl font-bold">Handle Failures</h3>
  </div>
  
  <div class="text-center">
    <div class="text-8xl mb-6">⚡</div>
    <h3 class="text-3xl font-bold">Parallelize</h3>
  </div>
  
  <div class="text-center">
    <div class="text-8xl mb-6">📍</div>
    <h3 class="text-3xl font-bold">Track State</h3>
  </div>
  
  <div class="text-center">
    <div class="text-8xl mb-6">🗄️</div>
    <h3 class="text-3xl font-bold">Real Databases</h3>
  </div>
</div>

---
layout: section
---

# Part 5: Evaluation

---
layout: default
---

# Systematic Evaluation

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="space-y-4">
    <h3 class="text-lg font-bold">📝 Build test sets:</h3>
    <ul class="text-sm space-y-1">
      <li>Real examples from your data</li>
      <li>The weird edge cases</li>
      <li>What failed before</li>
    </ul>
  </div>

  <div class="space-y-4">
    <h3 class="text-lg font-bold">🎯 Test what matters:</h3>
    <ul class="text-sm space-y-1">
      <li>Accuracy on YOUR data</li>
      <li>How it fails (not just how often)</li>
      <li class="text-orange-500 font-bold">What keeps me up at night?</li>
    </ul>
  </div>
</div>

---
layout: two-cols
---

# Make Iteration Painless

<div class="flex flex-col items-center justify-center">
  <img src="/images/make iteration painless.png" />
</div>

---
layout: section
---

# Part 6: Building A Couple More Blocks

---
layout: default
---

# From One-Off Script to Product

<div class="text-center mt-12">
  <div class="text-2xl mb-8">
    <span class="text-6xl">📝</span> → <span class="text-6xl">🤖</span>
  </div>
  
  <p class="text-3xl font-bold mb-6">Built an automated tool that:</p>
  
  <div class="text-2xl space-y-3">
    <p>✓ Takes any public comment dataset</p>
    <p>✓ Discovers the arguments automatically</p>
    <p>✓ Writes its own classification prompts</p>
    <p>✓ Runs fully autonomous analysis</p>
  </div>
  
  <div class="mt-10 text-xl italic text-gray-600">
    Structured output/Enum is still the secret sauce
  </div>
</div>

---
layout: center
---

# I Built A Couple More Blocks

<div class="flex flex-col items-center justify-center">
  <img src="/images/enum website gui.png" style="width: 50%; height: auto;" />
</div>

---
layout: default
---

# New Analyis!

<div class="flex flex-col items-center justify-center">
  <img src="/images/website.jpg" style="width: 80%; height: auto;" />
</div>

---
layout: center
class: text-center
---

# Find Me on the Internet!

🌐 <a href="https://abigailhaddad.netlify.app/" class="text-blue-600 text-3xl">abigailhaddad.netlify.app</a>

<div class="mt-12 text-2xl">
  <p class="font-bold mb-4">Want to hire me to consult?</p>
  <p>Fill out the form on my website!</p>
</div>

<div class="mt-8 text-xl">
  <p>Also find me on:</p>
  <p>🔗 <a href="https://github.com/abigailhaddad" class="text-blue-600">github.com/abigailhaddad</a></p>
  <p>📝 <a href="https://presentofcoding.substack.com" class="text-blue-600">presentofcoding.substack.com</a></p>
  <p>💻 <a href="https://github.com/abigailhaddad/rny_2025" class="text-blue-600">github.com/abigailhaddad/rny_2025</a> (this presentation)</p>
</div>

<style>
/* Keep only the image sizing that works */
.slide-image {
  @apply mx-auto my-6 max-h-64 object-contain;
}

.slide-image-small {
  @apply mx-auto my-4 max-h-48 object-contain;
}

.slide-image-large {
  @apply mx-auto my-6 max-h-80 object-contain;
}
</style>
