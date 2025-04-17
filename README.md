---
marp: true
theme: gaia
size: 16:9
paginate: true
backgroundColor: white
footer: iMio - Avril 2025
style: |
  section footer {text-align: left;}
  section h1 {color: #e30289;}
  section.fs-small p {font-size: 22px;}
  section table {font-size: 22px;}
_paginate: skip
_class: lead
---

![bg left:35% 80%](logo-imio.png)

# HTMX

https://htmx.org/

Une approche HDA (Hypermedia Driven Application) du développement web.

**Sébastien Verbois**

---

# Sommaire

- Qu'est-ce que HTMX ?
- Une petite HDA réalisée avec HTMX, FastAPI et Chameleon
- HDA versus SPA

---

# HTML Hypermedia controlers

#### Balise `<a>` (HTML 1 - 1993)

```html
<a href="https://www.imio.be">iMio</a>
```

#### Balise `<form>` (HTML 2 - 1995)

```html
<form method="POST" action="https://www.imio.be/login">
  <input type="email" name="user_email" />
  <input type="password" name="user_password" />
  <button type="submit">Se connecter<button>
</form>
```

---

# HTMX

- Why should only \<a\> & \<form\> be able to make HTTP requests?
- Why should only click & submit events trigger them?
- Why should only GET & POST methods be available?
- Why should you only be able to replace the entire screen?

By removing these constraints, htmx completes HTML as a hypertext

---

# Exemples HTMX

### Delete button
```html
<button hx-trigger="click" hx-delete="/contacts/27" hx-target="#message">Delete</button>
<div id="message" />
```
### Mouseenter event
```html
<div hx-trigger="mouseenter" hx-get="/contacts/27" hx-target="#contacts" hx-swap="beforeend">
  Append contact 27
</div>
<div id="contacts"><h3>Liste des contacts</h3></div>
```

---

# Une petite application (1/2)

Une petite application CRUD réalisée avec HTMX, FastAPI et Chameleon.

- HTMX : <https://htmx.org/>
- FastAPI : <https://fastapi.tiangolo.com/>
- Chameleon : <https://pypi.org/project/fastapi_chameleon/> et <https://chameleon.readthedocs.io>

---

# Une petite application (2/2)

- Home page : FastAPI endpoint and Chameleon template
- Contacts page structure (Firefox inspector)
- Delete contact button
- Add contact form
- Search form : search input and reset button
- Asynchronous loading of the contact section

---

# Triptych Proposals

- <https://alexanderpetros.com/triptych/>

1. Support PUT, PATCH, and DELETE in HTML Forms
2. Button Actions
3. Partial Page Replacement

---

# SPA versus HDA

| Single Page Application (SPA)                             | Hypermedia Driven Application (HDA)  |
| --------------------------------------------------------- | ------------------------------------ |
| Frontend + API JSON + Backend                             | Fullstack                            |
| Endpoints JSON                                            | Endpoints HTML                       |
| Logique métier éclatée                                    | Logique métier uniquement en backend |
| Pression pour un backend JS                               | Libre du language pour le backend    |
| Dev API JSON + Dev Back + Dev Front                       | Dev "Full Stack"                     |
| Complexe                                                  | Simple                               |
| Architecture Client/Serveur                               | Architecture hypermedia HATEOAS      |
| Applications avec changements UI en cascade ou Hors ligne | Toutes les autres                    |

---

# JSON versus HTML

| JSON                         | HTML                                               |
| ---------------------------- | -------------------------------------------------- |
| Pas de sémantique            | Fournit une sémantique (h1, p, header, ...)        |
| Pas d'_Hypermedia controls_  | Contient des _Hypermedia controls_ (_a_ et _form_) |
| Pas de client générique      | Hypermedia client (le navigateur)                  |
| Pour les échanges de données | Pour les interactions avec un humain               |

- Voir <https://htmx.org/essays/hypermedia-clients/>

---

# Réferences

- Hypermedia: A Reintroduction : <https://hypermedia.systems/hypermedia-a-reintroduction/>
- Triptych Proposals (New Attributes for HTML) : <https://github.com/alexpetros/triptych>
- HTMX Presentation : <https://www.scalablepath.com/front-end/htmx>
- Do not use hx-boost : <https://unplannedobsolescence.com/blog/less-htmx-is-more/>

---

<!-- _class: fs-small -->

# Food for thought

Any software project has a complexity budget, explicit or not: there is only so much complexity a given development team can tolerate and every new feature and implementation choice adds at least a bit more to the overall complexity of the system.

What is particularly nasty about complexity is that it tends to grow exponentially: one day you can keep the entire system in your head and understand the ramifications of a particular change, and a week later the whole system seems intractable. Even worse, efforts to help control complexity, such as introducing abstractions or infrastructure to manage the complexity, often end up making things even more complex. **Truly, the job of the good software engineer is to keep complexity under control.**

**The sure-fire way to keep complexity down is also the hardest: say no.** Pushing back on feature requests is an art and, if you can learn to do it well, making people feel like they said no, you will go far.

Sadly this is not always possible: some features will need to be built. At this point the question becomes: **“what is the simplest thing that could possibly work?”** Understanding the possibilities available in the hypermedia approach will give you another tool in your “simplest thing” tool chest.
