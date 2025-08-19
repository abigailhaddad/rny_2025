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

# Part 1: A Deadline

---
layout: default
---

# My Self-Imposed Deadline

<div class="flex flex-col items-center justify-center">
  <img src="/images/hourglass.png" class="w-95 h-95" />
</div>

**35K comments**

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

✅ 35,000 comments processed

🚀 Website live in days

⏰ Avoided: months of manual work

Two blocks deleted:
~~OCR~~
~~Gibberish Detector~~

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

# What Are You Trying to Do?

<div class="grid grid-cols-2 gap-16 mt-12">
  <div>
    <h2 class="font-bold mb-8">📄 Your Documents</h2>
    <div class="space-y-6">
      <p>✓ Clean PDFs?</p>
      <p>✓ Scanned images?</p>
      <p>✓ Mixed formats?</p>
      <p>✓ Handwritten?</p>
    </div>
  </div>
  
  <div>
    <h2 class="font-bold mb-8">🎯 Your Goals</h2>
    <div class="space-y-6">
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

# Your Equation

Your documents

+

Your goals

+

Your constraints

=

**Your solution**

---
layout: center
---

# Should I Throw It Into an LLM?

**MAYBE!!!**

---
layout: default
---

# Four Factors to Consider

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-blue-100 p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">🎯 Accuracy</h3>
    <ul class="space-y-2">
      <li>How good is good enough?</li>
      <li>How does it fail?</li>
    </ul>
  </div>
  
  <div class="bg-green-100 p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">🔍 Transparency</h3>
    <ul class="space-y-2">
      <li>Need deterministic output?</li>
      <li>Must explain decisions?</li>
    </ul>
  </div>
  
  <div class="bg-orange-100 p-6 rounded-lg">
    <h3 class="text-xl mb-4 font-bold">💰 Resources</h3>
    <ul class="space-y-2">
      <li>Can data leave your servers?</li>
      <li>API costs acceptable?</li>
    </ul>
  </div>
  
  <div class="bg-purple-100 p-6 rounded-lg">
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

**Mix and match based on your needs**

---
layout: default
---

# Remember My Seven Cents?

**Gemini only worked because:**

✓ Data could leave my environment

✓ 35,000 documents, most with no attachments = small enough for the budget

**Different constraints = Different solution**

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

### Define Your Data Contract
Everyone needs to agree on formats

### Lock Down Field Names
Changes break downstream systems

### Validate Everything
Don't trust, verify

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

### ❌ Don't:

```python
"Please only respond with 
'support' or 'oppose'"

# Hope it listens...
```

</div>
<div class="bg-green-100 p-10 rounded-lg">

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

### 📝 Build test sets:
- Real examples from your data
- The weird edge cases
- What failed before

### 🎯 Test what matters:
- Accuracy on YOUR data
- How it fails (not just how often)
- **What keeps me up at night?**

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

🔧 → 🏭

**One-off script → Reusable pipeline**

**Next project? Hours.**

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
