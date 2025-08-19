---
theme: seriph
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

<style>
.slidev-layout h1 {
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>

---
layout: section
---

# Part 1: A Deadline

---
layout: default
---

# My Self-Imposed Deadline

<div class="flex flex-col items-center justify-center">
  <img src="/images/hourglass.png" class="w-95 h-95" />
  <div class="mt-8 text-xl font-bold text-orange-500">
    35K comments
  </div>
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

<div class="space-y-8 font-semibold">
  <p>📄 Dark scanned PDFs</p>
  <p>🎭 Random meme attachments</p>
  <p>📸 Blurry photos of handwritten notes</p>
</div>

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

<div class="text-6xl font-black text-orange-500 animate-bounce">
  It Works!! 🎉🎊🥳
</div>

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

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="space-y-6 text-xl">
    <div class="flex items-center gap-4">
      <span class="text-green-500 text-xl">✅</span>
      <span>35,000 comments processed</span>
    </div>
    <div class="flex items-center gap-4">
      <span class="text-xl">🚀</span>
      <span>Website live in days</span>
    </div>
    <div class="flex items-center gap-4">
      <span class="text-xl">⏰</span>
      <span>Avoided: months of manual work</span>
    </div>
  </div>
  <div class="flex items-center">
    <div class="text-xl">
      Two blocks deleted:<br/>
      <span class="line-through text-red-500">OCR</span><br/>
      <span class="line-through text-red-500">Gibberish Detector</span>
    </div>
  </div>
</div>

---
layout: center
---

# Here It Is


<div class="flex flex-col items-center justify-center">
<img src="/images/comment_site.jpg" class="w-100 h-100" />
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

<div class="space-y-10 mt-12 text-center">
  <div class="text-4xl font-bold text-gray-700">"Is this fraudulent?"</div>
  <div class="text-4xl font-bold text-gray-700">"Should we interview them?"</div>
  <div class="text-4xl font-bold text-gray-700">"What's the main complaint?"</div>
</div>

<div class="mt-16 p-8 bg-blue-100 rounded-xl">
  <p class="text-3xl font-bold text-blue-700">
    ⏰ Time is the only barrier
  </p>
</div>

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

<div class="space-y-8 mt-8">
  <div>
    <h3 class="text-blue-600 font-bold">GET</h3>
    <p>Pull text from PDFs, Word docs, APIs, or user input</p>
  </div>
  
  <div>
    <h3 class="text-blue-600 font-bold">PROCESS</h3>
    <p>Use LLMs, regex, BERT, or other tools to extract meaning</p>
  </div>
  
  <div>
    <h3 class="text-blue-600 font-bold">DO</h3>
    <p>Create visualizations, populate templates, or trigger actions</p>
  </div>
</div>

::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/get process do blocks.png" />
</div>

---
layout: section
---

# Part 3: How to Get Started

---
layout: two-cols
---

# What Are You Trying to Do?

<div class="grid grid-cols-2 gap-16 mt-12">
  <div>
    <h2 class="text-4xl font-bold text-blue-600 mb-8">📄 Your Documents</h2>
    <div class="space-y-6 text-2xl">
      <p>✓ Clean PDFs?</p>
      <p>✓ Scanned images?</p>
      <p>✓ Mixed formats?</p>
      <p>✓ Handwritten?</p>
    </div>
  </div>
  
  <div>
    <h2 class="text-4xl font-bold text-green-600 mb-8">🎯 Your Goals</h2>
    <div class="space-y-6 text-2xl">
      <p>→ Extract fields?</p>
      <p>→ Classify docs?</p>
      <p>→ Summarize?</p>
      <p>→ Find patterns?</p>
    </div>
  </div>
</div>

---
layout: default
---

# Don't Forget Your Constraints

<div class="grid grid-cols-2 gap-8 mt-12">
  <div class="text-center p-8">
    <div class="text-6xl mb-4">🔒</div>
    <h3 class="text-3xl font-bold text-blue-600">Privacy</h3>
    <p class="text-2xl mt-2">Can data leave?</p>
  </div>
  
  <div class="text-center p-8">
    <div class="text-6xl mb-4">💰</div>
    <h3 class="text-3xl font-bold text-green-600">Budget</h3>
    <p class="text-2xl mt-2">API costs OK?</p>
  </div>
  
  <div class="text-center p-8">
    <div class="text-6xl mb-4">⏰</div>
    <h3 class="text-3xl font-bold text-orange-600">Time</h3>
    <p class="text-2xl mt-2">One-off or ongoing?</p>
  </div>
  
  <div class="text-center p-8">
    <div class="text-6xl mb-4">📊</div>
    <h3 class="text-3xl font-bold text-purple-600">Explain</h3>
    <p class="text-2xl mt-2">Show your work?</p>
  </div>
</div>

---
layout: center
---

# Your Equation

<div class="text-center space-y-8 text-xl mt-8">
  <div>Your documents</div>
  <div>+</div>
  <div>Your goals</div>
  <div>+</div>
  <div>Your constraints</div>
  <div>=</div>
  <div  class="text-xl font-bold text-blue-600">Your solution</div>
</div>

---
layout: center
---

# Should I Throw It Into an LLM?

<div  class="text-6xl font-black text-orange-500 mt-8 animate-pulse">
  MAYBE!!!
</div>

---
layout: default
---

# Four Factors to Consider

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-blue-600 text-white p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">🎯 Accuracy</h3>
    <ul class="space-y-2">
      <li>How good is good enough?</li>
      <li>How does it fail?</li>
    </ul>
  </div>
  
  <div class="bg-green-600 text-white p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">🔍 Transparency</h3>
    <ul class="space-y-2">
      <li>Need deterministic output?</li>
      <li>Must explain decisions?</li>
    </ul>
  </div>
  
  <div class="bg-orange-600 text-white p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">💰 Resources</h3>
    <ul class="space-y-2">
      <li>Can data leave your servers?</li>
      <li>API costs acceptable?</li>
    </ul>
  </div>
  
  <div class="bg-purple-600 text-white p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">⏰ Timeline</h3>
    <ul class="space-y-2">
      <li>Single batch or production?</li>
      <li>Who monitors failures?</li>
    </ul>
  </div>
</div>

---
layout: default
---

# When to Use What

| **📏 Rule-based** | **🤖 Smaller Models** | **🧠 LLMs** |
|---|---|---|
| Regex, keywords | BERT, spaCy | GPT-4, Claude |
| ✓ Simple patterns | ✓ Run locally | ✓ Complex tasks |
| ✓ Explainable | ✓ Single purpose | ✓ Flexible |

<div class="mt-8 text-center text-lg font-bold text-blue-600">
  Mix and match based on your needs
</div>

---
layout: default
---

# Remember My Seven Cents?

<div class="space-y-8 mt-8 text-xl">
  <div class="font-bold">Gemini only worked because:</div>
  
  <div class="flex items-center gap-4 ml-8">
    <span class="text-green-500 text-xl">✓</span>
    <span>Data could leave my environment</span>
  </div>
  
  <div class="flex items-center gap-4 ml-8">
    <span class="text-green-500 text-xl">✓</span>
    <span>35,000 documents, most with no attachments = small enough for the budget</span>
  </div>
  
  <div class="mt-8 text-center font-bold text-blue-600">
    Different constraints = Different solution
  </div>
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
  <p>Each use case needs <span class="text-blue-600 font-bold">different blocks</span></p>
  <p class="mt-2">What works for one project <span class="text-blue-600 font-bold">won't work for the next</span></p>

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

<div class="space-y-6 mt-8">
  <div>
    <h3 class="text-xl font-bold text-blue-600">Define Your Data Contract</h3>
    <p>Everyone needs to agree on formats</p>
  </div>
  
  <div>
    <h3 class="text-xl font-bold text-blue-600">Lock Down Field Names</h3>
    <p>Changes break downstream systems</p>
  </div>
  
  <div>
    <h3 class="text-xl font-bold text-blue-600">Validate Everything</h3>
    <p>Don't trust, verify</p>
  </div>
</div>

::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/schema.png" />
</div>

---
layout: default
---

# Enforce Structured Output

<div class="grid grid-cols-2 gap-8 mt-8">
<div class="bg-red-100 p-10 rounded-lg">

<h3 class="text-red-600 text-3xl font-bold mb-6">❌ Don't:</h3>

```python
"Please only respond with 
'support' or 'oppose'"

# Hope it listens...
```

</div>
<div class="bg-green-100 p-10 rounded-lg">

<h3 class="text-green-600 text-3xl font-bold mb-6">✅ Do:</h3>

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

<div class="space-y-4 mt-6">
  <p>Build modularity into your processing layer:</p>
  
  <ul class="space-y-3 mt-4">
    <li >Swap models without changing code</li>
    <li >Test multiple prompts in parallel</li>
    <li >Compare results side-by-side</li>
    <li >Grid search across configurations</li>
  </ul>
  
  <p  class="mt-6 font-bold text-blue-600">
    Modular design enables rapid experimentation
  </p>
</div>

::right::

<div class="flex items-center justify-center h-full">
  <img src="/images/make iteration painless.png" />
</div>

---
layout: default
---

# Production Monitoring

**For production systems, add a fourth step:**

- 🏷️ **Natural labeling** - Ground truth emerges over time
- 📊 **Performance tracking** - Know when models drift  
- 🎯 **Strategic sampling** - Human review of edge cases
- 🚨 **Failure alerts** - Catch problems early

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

<div class="flex items-center justify-center h-full">
  <div class="text-center">
    <div class="text-6xl mb-8">🔧 → 🏭</div>
    <div class="text-2xl font-bold">
      One-off script → Reusable pipeline
    </div>
    <div class="text-4xl font-black text-orange-500 mt-8">
      Next project? Hours.
    </div>
  </div>
</div>

---
layout: center
class: text-center
---

# Contact Me

<div class="mt-8 space-y-4 text-xl">
  <div>
    🔗 <a href="https://github.com/abigailhaddad" class="text-blue-600">github.com/abigailhaddad</a>
  </div>
  
  <div>
    📝 <a href="https://presentofcoding.substack.com" class="text-blue-600">presentofcoding.substack.com</a>
  </div>
</div>

<style>
/* Custom animations */
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}

.animate-float {
  animation: float 3s ease-in-out infinite;
}

/* Better code blocks */
pre {
  @apply bg-gray-100 p-4 rounded-lg overflow-x-auto;
}

/* Gradient backgrounds for sections */
.slidev-layout.section {
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
  color: white;
}

.slidev-layout.section h1 {
  color: white !important;
}

/* Standardized slide layouts - LARGER for back of room */
.slidev-layout {
  font-size: 36px !important;
  line-height: 1.6;
}

.slidev-layout h1 {
  @apply font-bold mb-8;
  font-size: 72px !important;
}

.slidev-layout h2 {
  @apply font-bold mb-6;
  font-size: 56px !important;
}

.slidev-layout h3 {
  @apply font-bold mb-4;
  font-size: 44px !important;
}

.slidev-layout p, .slidev-layout li {
  font-size: 36px !important;
  line-height: 1.8;
}

.slidev-layout ul, .slidev-layout ol {
  @apply space-y-3;
}

/* Make gray text lighter for better visibility */
.slidev-layout .text-gray-700 {
  @apply text-gray-500;
}

.slide-content {
  @apply mt-8;
}

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
