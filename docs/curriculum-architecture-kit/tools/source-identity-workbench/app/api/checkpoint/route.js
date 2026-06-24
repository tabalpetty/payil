import { NextResponse } from "next/server";
import { buildCheckpoint, checkpointMarkdown } from "../../lib/checkpoint";

export async function POST(request) {
  const input = await request.json();
  const checkpoint = buildCheckpoint(input);
  const markdown = checkpointMarkdown(checkpoint);
  return NextResponse.json({ checkpoint, markdown });
}

