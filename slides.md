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
---

# Processing Document Collections with LLMs
## A Practical Workflow

**Abigail Haddad**

---
layout: section
---

# Part 1: The Project

<!--
In May, I left my job. And I wanted to do a project that was both useful and showcased the kind of work I'd been doing.
-->

---
layout: default
---

# Comments Analysis

<div class="flex flex-col items-center justify-center">
  <img src="/images/regulations.jpg" style="width: 90%; height: auto;" />
</div>

---
layout: default
---

# My Self-Imposed Deadline

<div class="flex flex-col items-center justify-center">
  <img src="/images/hourglass.png" class="w-95 h-95" />
35K comments
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

# The Result

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="border-2 rounded-lg p-6 text-center">
    <div class="text-5xl mb-4">✅</div>
    <div class="text-2xl font-bold">35,000</div>
    <div>comments processed</div>
  </div>
  
  <div class="border-2 rounded-lg p-6 text-center">
    <div class="text-5xl mb-4">🚀</div>
    <div class="text-2xl font-bold">Days</div>
    <div>to launch website</div>
  </div>
  
  <div class="border-2 rounded-lg p-6 text-center">
    <div class="text-5xl mb-4">⏰</div>
    <div class="text-2xl font-bold">Months</div>
    <div>of manual work avoided</div>
  </div>
  
  <div class="border-2 rounded-lg p-6 text-center">
    <div class="text-5xl mb-4">🗑️</div>
    <div class="text-xl">Blocks deleted:</div>
    <div class="text-sm mt-2">~~OCR~~<br/>~~Gibberish Detector~~</div>
  </div>
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

# Part 2: A Step Back
## The Text Data Pipeline

---
layout: default
---

# Every Organization Has These

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

# Not RAG: Same Questions Each Time

**"Is this fraudulent?"**

**"Should we interview them?"**

**"What's the main complaint?"**

**⏰ Time is the only barrier**

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
layout: section
---

# Part 3: How to Get Started

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
layout: section
---

# Part 4: Real World Lessons

---
layout: default
---

# You Can't Build All The Blocks


<div class="flex flex-col items-center justify-center">
<img src="/images/too many blocks.png" class="w-70 h-70" />
</div>
Each use case needs **different blocks**

What works for one project **won't work for the next**

---
layout: default
---

# Scaling Up: Key Lessons

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
layout: two-cols
---

# Working With Teams


* Lock Down Field Names and Formats
* Validate Everything


::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/schema.png" />
</div>

---
layout: default
---

# Enforce Structured Output

<div class="grid grid-cols-2 gap-8 mt-8">
<div class="bg-red-100 p-10 rounded-lg text-red-900">

### ❌ Don't:

```python
"Please only respond with 
'support' or 'oppose'"

# Hope it listens...
```

</div>
<div class="bg-green-100 p-10 rounded-lg text-green-900">

### ✅ Do:

```python
class StanceEnum(str, Enum):
    support = 'support'
    oppose = 'oppose'
```

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

Build modularity into your processing layer:

- Swap models without changing code
- Test multiple prompts in parallel
- Compare results side-by-side
- Grid search across configurations

**Modular design enables rapid experimentation**

::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/make iteration painless.png" />
</div>

---
layout: default
---

# Production Monitoring

**For production systems, add a fourth step:**

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="border rounded p-4">
    <div class="text-3xl mb-2">🏷️</div>
    <div class="font-bold">Natural labeling</div>
    <div class="text-sm">Ground truth emerges over time</div>
  </div>
  
  <div class="border rounded p-4">
    <div class="text-3xl mb-2">📊</div>
    <div class="font-bold">Performance tracking</div>
    <div class="text-sm">Know when models drift</div>
  </div>
  
  <div class="border rounded p-4">
    <div class="text-3xl mb-2">🎯</div>
    <div class="font-bold">Strategic sampling</div>
    <div class="text-sm">Human review of edge cases</div>
  </div>
  
  <div class="border rounded p-4">
    <div class="text-3xl mb-2">🚨</div>
    <div class="font-bold">Failure alerts</div>
    <div class="text-sm">Catch problems early</div>
  </div>
</div>

---
layout: section
---

# Part 6: Conclusion

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

# The Real Win

<div class="flex items-center justify-center gap-8 mt-16">
  <div class="text-center">
    <div class="text-8xl mb-4">🔧</div>
    <div class="text-xl">One-off script</div>
  </div>
  
  <div class="text-6xl">→</div>
  
  <div class="text-center">
    <div class="text-8xl mb-4">🏭</div>
    <div class="text-xl">Reusable pipeline</div>
  </div>
</div>

<div class="mt-16 text-center">
  <div class="text-4xl font-bold border-4 p-6 rounded-lg inline-block">
    Next project? Hours. ⚡
  </div>
</div>

---
layout: center
class: text-center
---

# Contact Me

🔗 <a href="https://github.com/abigailhaddad" class="text-blue-600">github.com/abigailhaddad</a>

📝 <a href="https://presentofcoding.substack.com" class="text-blue-600">presentofcoding.substack.com</a>

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
