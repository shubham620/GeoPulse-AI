from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def verify_events(text_list):

    embeddings = model.encode(text_list)

    verified_events = []

    for i in range(len(text_list)):
        for j in range(i + 1, len(text_list)):

            similarity = util.cos_sim(embeddings[i], embeddings[j])

            if similarity > 0.75:
                verified_events.append((text_list[i], text_list[j], float(similarity)))

    return verified_events