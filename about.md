---
layout: default
title: About
permalink: /about/
footer_offset: 71%
footer_gap: 140
portrait: { src: /assets/img/portrait-1.jpg }
facts:
  - { k: born, v: "Pula, 1996" }
  - { k: studied, v: "ADU Zagreb · Uniarts Helsinki · SNDO Amsterdam · Blank film school" }
  - { k: company, v: "Zagrebački plesni ansambl" }
  - { k: curating, v: "Improspekcije 2024, 2025" }
  - { k: residencies, v: "Life Long Burning, Budapest 2026 · Jelsa Art Biennial 2023" }
  - { k: award, v: "Best Performance Overall, 2024 (UPUH & UPPU PULS)" }
  - { k: shortlist, v: "Zlatna lubenica young artist award, finalist 2020" }
elsewhere:
  - { label: "instagram ↗", url: "https://www.instagram.com/dorabrkaric/" }
  - { label: "vimeo ↗", url: "https://vimeo.com/user95667145" }
  - { label: "zpa ↗", url: "https://www.zagrebackiplesniansambl.hr/hr/tim/dora-brkaric.html" }
  - { label: "kulturpunkt ↗", url: "https://kulturpunkt.hr/tag/dora_brkaric/" }
---
<h1 class="vh">About Dora Brkarić</h1>

<div class="about-row mt-110">
{% include placeholder.html src=page.portrait.src ratio="2 / 3" tone=1 caption=page.portrait.caption alt="Portrait of Dora Brkarić" class="portrait off x9" %}
<div class="bio" markdown="1">

Dora Brkarić (b. 1996, Pula) is a contemporary dance artist and choreographer working in [Zagreb and Istria]. She studied contemporary dance at the Academy of Dramatic Art in Zagreb and continued her training in choreography at Uniarts Helsinki and SNDO Amsterdam.

Her work strips back identity, looks at what is repressed and how present a body can be — and often leaves the theatre for galleries, video and film. [S T R I P T E A S E]({{ '/works/striptease/' | relative_url }}), made with Iva Katarinčić, won Best Performance Overall at the Croatian contemporary dance awards for 2024.

As a performer she has worked with Matej Kejžar, Simone Aughterlony & Saša Božić, Flavia Pinheiro, Marin Lemić, Matea Bilosnić and Igor x Moreno. She is a permanent member of Zagrebački plesni ansambl and co-curates Improspekcije, Zagreb's festival of improvisation.

</div>
</div>

<dl class="facts off x61 mt-200">
{%- for f in page.facts %}
  <dt>{{ f.k }}</dt><dd>{{ f.v }}</dd>
{%- endfor %}
</dl>

<section class="elsewhere off x4 mt-180">
  <h2 class="sublabel">elsewhere</h2>
  <ul>
  {%- for l in page.elsewhere %}
    <li><a href="{{ l.url }}">{{ l.label }}</a></li>
  {%- endfor %}
  </ul>
</section>

<section class="elsewhere off x4 mt-120">
  <h2 class="sublabel">contact</h2>
  <ul>
    <li><a href="mailto:{{ site.contact_email }}">email</a></li>
  </ul>
</section>
