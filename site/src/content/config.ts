import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const entries = defineCollection({
  loader: glob({ pattern: '**/*.yaml', base: '../../data/services' }),
  schema: z.object({
    service: z.string(),
    control_domain: z.string(),
    overall: z.enum(['aws', 'customer', 'shared', 'model_provider', 'not_stated']),
    responsibility: z.object({
      aws: z.string().nullable().optional(),
      customer: z.string().nullable().optional(),
      model_provider: z.string().nullable().optional(),
    }).optional(),
    default_state: z.object({
      enabled_by_default: z.boolean().nullable().optional(),
      since: z.string().nullable().optional(),
    }).optional(),
    sources: z.array(z.object({
      url: z.string(),
      quote: z.string().optional(),
      retrieved: z.string().optional(),
      content_hash: z.string().optional(),
      source_type: z.string().optional(),
    })).optional(),
    review: z.object({
      status: z.string(),
      reviewed_on: z.string(),
      confidence: z.string().optional(),
      rationale: z.string().optional(),
    }),
    frameworks: z.record(z.any()).optional(),
    customer_actions: z.array(z.any()).optional(),
    deployment_scope: z.string().nullable().optional(),
    sub_feature: z.string().nullable().optional(),
    layer: z.string().nullable().optional(),
    contractual: z.boolean().optional(),
  }),
});

export const collections = { entries };